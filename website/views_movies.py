import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

#TODO: Implement off of the views_employee.py file.

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



@views_movies.route( "/edit_movie/<int:id>" , methods = [ "GET" , "POST" ] )
def edit_movie( id ) :

    pass

@views_movies.route( "/delete_movie/<int:id>" , methods = [ "GET" , "POST" ] )
def delete_movie( id ) :

    pass

