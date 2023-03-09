import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

#TODO: Implement off of the views_employee.py file. THIS DONE

views_movies = Blueprint('views_movies', __name__)
# connect to database
db_connection = db.connect_to_database()

@views_movies.route('/movies', methods=["POST", "GET"])
def movies():
    if request.method == "GET":
        query = "SELECT * FROM Movies;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
        return render_template("movies.html", movies=result)

    if request.method == "POST" :

        title = request.form[ "title" ]

        stock = request.form[ "stock" ]

        price = request.form[ "price" ]

        query = "INSERT INTO Movies ( title , stock , price ) VALUES ( %s , %s , %s ) ; "

        query_params = ( title , stock , price )

        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
        script.flashMessage(crud='create')


        return redirect( "/movies" )

@views_movies.route( "/edit_movie/<int:id>" , methods = [ "GET" , "POST" ] )
def edit_movie( id ) :

    if request.method == "GET" :


        query = "SELECT * FROM Movies WHERE movie_id = %s ; "
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
        result = cursor.fetchall()
        return render_template("edit/edit_movie.html", movies=result)


    if request.method == "POST" :

        title = request.form["title"]
        stock = request.form["stock"]

        price = request.form["price"]

        query = "UPDATE Movies SET title = %s , stock = %s , price = %s WHERE movie_id = %s ; "

        query_params = ( title , stock , price )
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
        script.flashMessage(crud='update')
        return redirect('/movies ')







@views_movies.route( "/delete_movie/<int:id>" , methods = [ "GET" , "POST" ] )
def delete_movie( id ) :
    query = "DELETE FROM Movies WHERE id = '%s';"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    time.sleep(1)
    return redirect("/movies")



