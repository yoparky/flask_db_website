from flask import Blueprint, redirect, render_template, json, flash, request
from .database import db_connector as db

# All views here
views = Blueprint('views', __name__)
# connect to database
db_connection = db.connect_to_database()

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/reset_db')
def reset_db():
    query = "DELETE FROM Employees WHERE id = '%s';"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect("/employees")

@views.route('/employees', methods=["POST", "GET"])
def employees():
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
            flash('First name must be greater than 1 character', category='error')
        elif len(lname) < 2:
            flash('Last name must be greater than 1 character', category='error')
        elif len(strname) < 2:
            flash('Street name must be greater than 1 character', category='error')
        elif len(cityname) < 2:
            flash('City name must be greater than 1 character', category='error')
        elif len(stname) < 2:
            flash('State name must be greater than 1 character', category='error')
        elif len(phone) < 10:
            flash('Phone number must be greater than 9 character', category='error')
        else:
            # add to db
            query = "INSERT INTO Employees (first, last, street, city, state, phone) VALUES (%s, %s, %s, %s, %s, %s)"
            query_params=(fname, lname, strname, cityname, stname, phone)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            # flash success
            flash('Entry added to database!', category='success')

    # Default to GET behavior and update table if entry added
    query = "SELECT * FROM Employees;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    result = cursor.fetchall()
    # a potential query2 that populates the dropdown etc.
    return render_template("employees.html", employees=result)

@views.route('/delete_employee/<int:id>')
def delete_employee(id):
    query = "DELETE FROM Employees WHERE id = '%s';"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    return redirect("/employees")

@views.route('/edit_employee/<int:id>', methods=["POST", "GET"])
def edit_employee_id(id):
    query = "SELECT * FROM Employees WHERE id = '%s';"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    result = cursor.fetchall()

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
            flash('First name must be greater than 1 character', category='error')
        elif len(lname) < 2:
            flash('Last name must be greater than 1 character', category='error')
        elif len(strname) < 2:
            flash('Street name must be greater than 1 character', category='error')
        elif len(cityname) < 2:
            flash('City name must be greater than 1 character', category='error')
        elif len(stname) < 2:
            flash('State name must be greater than 1 character', category='error')
        elif len(phone) < 10:
            flash('Phone number must be greater than 9 character', category='error')
        else:
            # add to db
            query = "UPDATE Employees SET first = %s, last = %s, street = %s, city = %s, state = %s, phone = %s WHERE id = %s"
            query_params=(fname, lname, strname, cityname, stname, phone, id)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            # flash success
            flash('Entry updated!', category='success')
            return redirect('/employees')

    # Default to GET behavior and update table if entry added
    query = "SELECT * FROM Employees WHERE id='%s';"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    result = cursor.fetchall()
    # a potential query2 that populates the dropdown etc.
    return render_template("edit/edit_employee.html", employees=result)

# TODO NEED TO IMPLEMENT FROM HERE DOWN.

@views.route('/customers', methods=["POST", "GET"])
def customers():
    if request.method == "GET":
        query = "SELECT * FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("customers.html", customers=result)

@views.route('/movies', methods=["POST", "GET"])
def movies():
    if request.method == "GET":
        query = "SELECT * FROM Movies;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("movies.html", movies=result)

@views.route('/actors', methods=["POST", "GET"])
def actors():
    if request.method == "GET":
        query = "SELECT * FROM Actors;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("actors.html", actors=result)

@views.route('/order_items', methods=["POST", "GET"])
def order_items():
    if request.method == "GET":
        query = "SELECT * FROM Order_items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("order_items.html", order_items=result)

@views.route('/orders', methods=["POST", "GET"])
def orders():
    if request.method == "GET":
        query = "SELECT * FROM Orders;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("orders.html", orders=result)

@views.route('/performances', methods=["POST", "GET"])
def performances():
    if request.method == "GET":
        query = "SELECT * FROM Performances;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()
    return render_template("performances.html", performances=result)