import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

#TODO: Implement off of the views_employee.py file.

views_customers = Blueprint('views_customers', __name__)
# connect to database
db_connection = db.connect_to_database()

@views_customers.route('/customers', methods=["POST", "GET"])
def customers():
    if request.method == "GET":
        query = "SELECT * FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("customers.html", customers=result)