import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

#TODO: Implement off of the views_employee.py file. DONE THIS

views_actors = Blueprint('views_actors', __name__)
# connect to database
db_connection = db.connect_to_database()

@views_actors.route('/actors', methods=["POST", "GET"])
def actors():
    if request.method == "GET":
        query = "SELECT * FROM Actors;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
        return render_template("actors.html", actors=result)

    if request.method == "POST" :

        first = request.form[ "first" ]
        last = request.form[ "last" ]

        query = "INSERT INTO Actors ( first , last )  VALUES ( %s , %s ) ; "
        query_params = ( first , last )

        cursor = db.execute_query( db_connection = db_connection , query = query , query_params = query_params )
        script.flashMessage(crud='create')

        return redirect("/actors")

@views_actors.route( "/edit_actor/<int:id>" , methods = [ "GET" , "POST" ] )
def edit_actor( id ) :

    if request.method == "GET" :

        # Default to GET behavior and update table if entry added
        query = "SELECT * FROM Actors WHERE id='%s';"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
        result = cursor.fetchall()
        # a potential query2 that populates the dropdown etc.
        return render_template("edit/edit_employee.html", actors=result)

    if request.method == "POST" :
        first = request.form["first"]
        last = request.form["last"]

        query = "UPDATE Actors SET first = %s , last = %s WHERE actor_id = %s ; "
        query_params = (first, last)
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)

        script.flashMessage(crud='update')
        return redirect('/actors')


@views_actors.route( "/delete_actor/<int:id>" , methods = [ "GET" , "POST" ] )
def delete_actor( id ) :

    query = "DELETE FROM Actors WHERE id = '%s';"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    time.sleep(1)
    return redirect("/actors")



