import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

views_performances = Blueprint('views_performances', __name__)
db_connection = db.connect_to_database()

@views_performances.route('/performances', methods=["POST", "GET"])
def performances():
    if request.method == "POST":
        movie_id = request.form["movie_id"]
        actor_id = request.form["actor_id"]

        # validate - Should refactor
        if len(movie_id) < 1:
            script.flashMessage('Movie ID', 0, 'error')
        elif len(actor_id) < 1:
            script.flashMessage('Actor ID', 0, 'error')
        else:
            query = "INSERT INTO Performances (movie_id, actor_id) VALUES (%s, %s)"
            query_params = (movie_id, actor_id)
            db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            script.flashMessage(crud='create')

    query = """SELECT Performances.performance_id, Performances.movie_id, Movies.title AS movie_title, 
                Performances.actor_id FROM Performances 
                JOIN Movies ON Performances.movie_id = Movies.movie_id;"""
    performances = db.execute_query(db_connection=db_connection, query=query).fetchall()

    query_movies = "SELECT movie_id, title FROM Movies;"
    movies = db.execute_query(db_connection=db_connection, query=query_movies).fetchall()

    query_actors = "SELECT actor_id, CONCAT(first, ' ', last) AS name FROM Actors;"
    actors = db.execute_query(db_connection=db_connection, query=query_actors).fetchall()

    return render_template("performances.html", performances=performances, movies=movies, actors=actors)

@views_performances.route('/delete_performance/<int:id>')
def delete_performance(id):
    query = "DELETE FROM Performances WHERE performance_id = %s;"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    time.sleep(1)
    return redirect("/performances")

@views_performances.route('/edit_performance/<int:id>', methods=["POST", "GET"])
def edit_performance_id(id):
    if request.method == "POST":
        movie_id = request.form["movie_id"]
        actor_id = request.form["actor_id"]
        # validate -- refactor maybe
        if len(movie_id) < 1:
            script.flashMessage('Movie ID', 0, 'error')
        elif len(actor_id) < 1:
            script.flashMessage('Actor ID', 0, 'error')
        else:
            # add to db
            query = "UPDATE Performances SET movie_id = %s, actor_id = %s WHERE performance_id = %s"
            query_params = (movie_id, actor_id, id)
            db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            script.flashMessage(crud='update')
            return redirect('/performances')

    query = """SELECT Performances.performance_id, Performances.movie_id, Movies.title AS movie_title, 
               Performances.actor_id FROM Performances 
               JOIN Movies ON Performances.movie_id = Movies.movie_id
               WHERE performance_id = %s;"""
    performance = db.execute_query(db_connection=db_connection, query=query, query_params=(id,)).fetchone()

    query_movies = "SELECT movie_id, title FROM Movies;"
    movies = db.execute_query(db_connection=db_connection, query=query_movies).fetchall()

    query_actors = "SELECT actor_id, CONCAT(first, ' ', last) AS name FROM Actors;"
    actors = db.execute_query(db_connection=db_connection, query=query_actors).fetchall()

    return render_template("edit/edit_performance.html", performance=performance, movies=movies, actors=actors)