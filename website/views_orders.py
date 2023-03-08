import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

#TODO: Implement off of the views_employee.py file.

views_orders = Blueprint('views_orders', __name__)
# connect to database
db_connection = db.connect_to_database()

@views_orders.route('/orders', methods=["POST", "GET"])
def orders():
    if request.method == "GET":
        query = "SELECT * FROM Orders;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("orders.html", orders=result)