import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

#TODO: Implement off of the views_employee.py file.

views_order_items = Blueprint('views_order_items', __name__)
# connect to database
db_connection = db.connect_to_database()

@views_order_items.route('/order_items', methods=["POST", "GET"])
def order_items():
    if request.method == "GET":
        query = "SELECT * FROM Order_items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("order_items.html", order_items=result)