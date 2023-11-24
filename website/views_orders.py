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
    if request.method == "POST":
        # grab input
        employee_selection = request.form["employee_selection"]
        customer_selection = request.form["customer_selection"]
        orderdate = request.form["orderdate"]
        cnum = request.form["cnum"]
        ofulfill = request.form["ofulfill"]
        # validate - Should refactor
        if len(orderdate) < 1:
            script.flashMessage('Date', 1, 'error')
        elif len(cnum) < 15:
            script.flashMessage('Credit Card Number', 15, 'error')
        elif ofulfill != '1' and ofulfill != '0':
            script.flashMessage('Order Fulfilled', 1, 'error')
        else:
            # add to db
            query = "INSERT INTO Orders (customer_id, employee_id, order_date, credit_card_num, order_fulfilled) VALUES (%s, %s, %s, %s, %s)"
            query_params=(customer_selection, employee_selection, orderdate, cnum, ofulfill)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            # flash success
            script.flashMessage(crud='create')

    # Default to GET behavior and update table if entry added
    query1 = """SELECT Orders.order_id, 
                CONCAT_WS(', ', Customers.first, Customers.last) AS 'Customer Name', 
                CONCAT_WS(', ', Employees.first, Employees.last) AS 'Employee Name',
                Orders.order_date, Orders.credit_card_num, Orders.order_fulfilled
                FROM Orders
                INNER JOIN Customers ON Orders.customer_id = Customers.id
                INNER JOIN Employees ON Orders.employee_id = Employees.id"""
    cursor = db.execute_query(db_connection=db_connection, query=query1)
    result = cursor.fetchall()
    query2 = "SELECT Employees.first, Employees.last, Employees.id FROM Employees"
    cursor2 = db.execute_query(db_connection=db_connection, query=query2)
    result2 = cursor2.fetchall()
    query3 = "SELECT Customers.first, Customers.last, Customers.id FROM Customers"
    cursor3 = db.execute_query(db_connection=db_connection, query=query3)
    result3 = cursor3.fetchall()

    return render_template("orders.html", orders=result, dropdown_employee=result2, dropdown_customer=result3)

@views_orders.route('/delete_order/<int:id>')
def delete_order(id):
    query = "DELETE FROM Orders WHERE order_id = '%s';"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    time.sleep(1)
    return redirect("/orders")

@views_orders.route('/edit_order/<int:id>', methods=["POST", "GET"])
def edit_order_id(id):

    if request.method == "POST":
        # grab input
        employee_selection = request.form["employee_selection"]
        customer_selection = request.form["customer_selection"]
        orderdate = request.form["orderdate"]
        cnum = request.form["cnum"]
        ofulfill = request.form["ofulfill"]
        # validate - Should refactor
        if len(orderdate) < 1:
            script.flashMessage('Date', 1, 'error')
        elif len(cnum) < 15:
            script.flashMessage('Credit Card Number', 15, 'error')
        elif ofulfill != '1' and ofulfill != '0':
            script.flashMessage('Order Fulfilled', 1, 'error')
        else:
            # add to db
            query = "UPDATE Orders SET employee_id = %s, customer_id = %s, order_date = %s, credit_card_num = %s, order_fulfilled = %s WHERE order_id = %s"
            query_params=(employee_selection, customer_selection, orderdate, cnum, ofulfill, id)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
            # flash success
            script.flashMessage(crud='update')
            return redirect('/orders')

    # Default to GET behavior and update table if entry added
    query = """SELECT Orders.order_id, 
                CONCAT_WS(', ', Customers.first, Customers.last) AS 'Customer Name', 
                CONCAT_WS(', ', Employees.first, Employees.last) AS 'Employee Name',
                Orders.order_date, Orders.credit_card_num, Orders.order_fulfilled
                FROM Orders
                   INNER JOIN Customers ON Orders.customer_id = Customers.id
                INNER JOIN Employees ON Orders.employee_id = Employees.id
                WHERE Orders.order_id='%s';
            """
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    result = cursor.fetchall()
    query2 = "SELECT Employees.first, Employees.last, Employees.id FROM Employees"
    cursor2 = db.execute_query(db_connection=db_connection, query=query2)
    result2 = cursor2.fetchall()
    query3 = "SELECT Customers.first, Customers.last, Customers.id FROM Customers"
    cursor3 = db.execute_query(db_connection=db_connection, query=query3)
    result3 = cursor3.fetchall()
    # a potential query2 that populates the dropdown etc.
    return render_template("edit/edit_order.html", orders=result, dropdown_employee=result2, dropdown_customer=result3)