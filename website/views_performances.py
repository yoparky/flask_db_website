import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

#TODO: Implement off of the views_employee.py file.

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


@views_performances.route('/edit_performance/<int:id>', methods=["POST", "GET"])
def edit_performance( id ) :

    pass

@views_performances.route('/delete_performance/<int:id>', methods=["POST", "GET"])
def delete_performance( id ) :

    pass

