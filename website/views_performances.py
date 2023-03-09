import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

#TODO: Implement off of the views_employee.py file. DONE THIS

views_performances = Blueprint('views_performances', __name__)
# connect to database
db_connection = db.connect_to_database()

@views_performances.route('/performances', methods=["POST", "GET"])
def performances():
    if request.method == "GET":
        query = "SELECT * FROM Performances;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()

        return render_template("performances.html", performances=result)

    if request.method == "POST" :

        movie_id = request.form["movie_id"]
        actor_id = request.form["actor_id"]

        query = "INSERT INTO Performances ( movie_id , actor_id ) VALUES ( %s , %s ) ; "
        query_params = ( movie_id , actor_id )
        cursor = db.execute_query( db_connection = db_connection , query = query , query_params = query_params )

        script.flashMessage(crud='create')

        return redirect( "/performances" )

@views_performances.route('/edit_performance/<int:id>', methods=["POST", "GET"])
def edit_performance( id ) :

    if request.method == "GET" :

        query = " SELECT * FROM Performances WHERE performance_id = %s ; "
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))

        result = cursor.fetchall()
        return render_template("edit/edit_performance.html", performances=result)

    if request.method == "POST" :

        movie_id = request.form["movie_id"]
        actor_id = request.form["actor_id"]

        query = "UPDATE Performances SET movie_id = %s , actor_id = %s WHERE performance_id = %s ; "

        query_params = ( movie_id , actor_id )
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)

        script.flashMessage(crud='update')
        return redirect('/performances')


@views_performances.route('/delete_performance/<int:id>', methods=["POST", "GET"])
def delete_performance( id ) :

    query = "DELETE FROM Performances WHERE performance_id = '%s';"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    time.sleep(1)
    return redirect("/performances")



