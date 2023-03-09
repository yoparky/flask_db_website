import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

views_actors = Blueprint('views_actors', __name__)
# connect to database
db_connection = db.connect_to_database()


@views_actors.route('/actors', methods=["POST", "GET"])
def actors():
    if request.method == "POST":
        # grab input
        fname = request.form["fname"]
        lname = request.form["lname"]
        # validate - Should refactor
        if len(fname) < 2:
            script.flashMessage('First name', 1, 'error')
        elif len(lname) < 2:
            script.flashMessage('Last name', 1, 'error')
        else:
            # add to db
            query = "INSERT INTO Actors (first, last) VALUES (%s, %s)"
            query_params=(fname, lname)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            # flash success
            script.flashMessage(crud='create')

    # Default to GET behavior and update table if entry added
    query = "SELECT * FROM Actors;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    result = cursor.fetchall()
    # a potential query2 that populates the dropdown etc.
    return render_template("actors.html", actors=result)

@views_actors.route('/delete_actor/<int:id>')
def delete_actor(id):
    query = "DELETE FROM Actors WHERE actor_id = '%s';"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    time.sleep(1)
    return redirect("/actors")

@views_actors.route('/edit_actor/<int:id>', methods=["POST", "GET"])
def edit_actor_id(id):

    if request.method == "POST":
        # grab input
        fname = request.form["fname"]
        lname = request.form["lname"]
        # validate -- refactor maybe
        if len(fname) < 2:
            script.flashMessage('First name', 1, 'error')
        elif len(lname) < 2:
            script.flashMessage('Last name', 1, 'error')
        else:
            # add to db
            query = "UPDATE Actors SET first = %s, last = %s WHERE actor_id = %s"
            query_params=(fname, lname, id)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            # flash success
            script.flashMessage(crud='update')
            return redirect('/actors')

    # Default to GET behavior and update table if entry added
    query = "SELECT * FROM Actors WHERE actor_id='%s';"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    result = cursor.fetchall()
    # a potential query2 that populates the dropdown etc.
    return render_template("edit/edit_actor.html", actors=result)