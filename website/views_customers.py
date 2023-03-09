import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

views_customers = Blueprint('views_customers', __name__)
# connect to database
db_connection = db.connect_to_database()


@views_customers.route('/customers', methods=["POST", "GET"])
def customers():
    if request.method == "POST":
        # grab input
        fname = request.form["fname"]
        lname = request.form["lname"]
        strname = request.form["strname"]
        cityname = request.form["cityname"]
        stname = request.form["stname"]
        phone = request.form["phone"]
        # validate - Should refactor
        if len(fname) < 2:
            script.flashMessage('First name', 1, 'error')
        elif len(lname) < 2:
            script.flashMessage('Last name', 1, 'error')
        elif len(strname) < 2:
            script.flashMessage('Street name', 1, 'error')
        elif len(cityname) < 2:
            script.flashMessage('City name', 1, 'error')
        elif len(stname) < 2:
            script.flashMessage('State name', 1, 'error')
        elif len(phone) < 10:
            script.flashMessage('Phone number', 9, 'error')
        else:
            # add to db
            query = "INSERT INTO Customers (first, last, street, city, state, phone) VALUES (%s, %s, %s, %s, %s, %s)"
            query_params=(fname, lname, strname, cityname, stname, phone)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            # flash success
            script.flashMessage(crud='create')

    # Default to GET behavior and update table if entry added
    query = "SELECT * FROM Customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    result = cursor.fetchall()
    # a potential query2 that populates the dropdown etc.
    return render_template("customers.html", customers=result)

@views_customers.route('/delete_customer/<int:id>')
def delete_customer(id):
    query = "DELETE FROM Customers WHERE id = '%s';"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    time.sleep(1)
    return redirect("/customers")

@views_customers.route('/edit_customer/<int:id>', methods=["POST", "GET"])
def edit_customer_id(id):

    if request.method == "POST":
        # grab input
        fname = request.form["fname"]
        lname = request.form["lname"]
        strname = request.form["strname"]
        cityname = request.form["cityname"]
        stname = request.form["stname"]
        phone = request.form["phone"]
        # validate -- refactor maybe
        if len(fname) < 2:
            script.flashMessage('First name', 1, 'error')
        elif len(lname) < 2:
            script.flashMessage('Last name', 1, 'error')
        elif len(strname) < 2:
            script.flashMessage('Street name', 1, 'error')
        elif len(cityname) < 2:
            script.flashMessage('City name', 1, 'error')
        elif len(stname) < 2:
            script.flashMessage('State name', 1, 'error')
        elif len(phone) < 10:
            script.flashMessage('Phone number', 9, 'error')
        else:
            # add to db
            query = "UPDATE Customers SET first = %s, last = %s, street = %s, city = %s, state = %s, phone = %s WHERE id = %s"
            query_params=(fname, lname, strname, cityname, stname, phone, id)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            # flash success
            script.flashMessage(crud='update')
            return redirect('/customers')

    # Default to GET behavior and update table if entry added
    query = "SELECT * FROM Customers WHERE id='%s';"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    result = cursor.fetchall()
    # a potential query2 that populates the dropdown etc.
    return render_template("edit/edit_customers.html", customers=result)