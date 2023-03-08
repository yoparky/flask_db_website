import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script


#TODO: Implement off of the views_employee.py file.

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