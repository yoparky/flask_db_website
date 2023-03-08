import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import script

# TODO: Implement off of the views_employee.py file.

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

    if request.method == "POST" :

        fname = request.form["fname"]
        lname = request.form["lname"]
        strname = request.form["strname"]
        cityname = request.form["cityname"]
        stname = request.form["stname"]
        phone = request.form["phone"]

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

            query = "INSERT INTO Customers ( first , last , street , city , state , phone ) values ( %s , %s , %s , %s , %s , %s ) ; "
            params = ( fname , lname , strname , cityname , stname , phone )

            cursor = db.execute_query( db_connection = db_connection , query = query , query_params= params)
            script.flashMessage( crud = "create" )

            return redirect( "/customers" )


@views_customers.route( "/delete_customer/<int:id>" , methods = [ "GET" , "POST" ] )
def delete_cusmoter( id ) :

    query = "DELETE FROM Customers WHERE id = '%s' ; "
    db.execute_query( db_connection = db_connection , query = query , query_params = ( id , ) )
    time.sleep( 1 )

    return redirect( "/customers")

@views_customers.route( "/edit_customer/<int:id>" , methods = [ "GET" , "POST" ] )
def edit_customer( id ) :

    if request.method == "GET" :

        query = "SELECT * FROM Customers WHERE id='%s';"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))

        customers = cursor.fetchall()
        return render_template("edit/edit_customer.html", customers=customers)

    if request.method == "POST" :

        fname = request.form["fname"]
        lname = request.form["lname"]

        strname = request.form["strname"]
        cityname = request.form["cityname"]

        stname = request.form["stname"]
        phone = request.form["phone"]

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

            query = "UPDATE Customers SET first = %s, last = %s, street = %s, city = %s, state = %s, phone = %s WHERE id = %s"
            query_params = (fname, lname, strname, cityname, stname, phone, id)

            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            script.flashMessage(crud='update')

            return redirect('/customers')

    return redirect('/customers')










