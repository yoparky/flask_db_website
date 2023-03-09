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

    if request.method == "POST" :

        order_id = request.form["order_id"]
        movie_id = request.form["movie_id"]

        quantity = request.form["quantity"]


        query = "INSERT INTO Order_items ( order_id , movie_id , quantity ) values ( %s , %s , %s ) ; "
        query_params = ( order_id , movie_id , quantity )
        cursor = db.execute_query( db_connection = db_connection , query = query , query_params = query_params )
        script.flashMessage(crud='create')

        return redirect("/order_items")

@views_order_items.route( "/edit_order_item/<int:id>" , methods = [ "GET" , "POST" ] )
def edit_order_item( id ) :

    if request.method == "GET" :

        query = "SELECT * FROM Order_items WHERE ( order_id , movie_id ) = %s  "
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
        result = cursor.fetchall()
        return render_template("edit/edit_order_items.html", order_items=result)


    if request.method == "POST" :

        quantity = request.form["quantity"]

        query = "UPDATE Order_items SET quantity = %s WHERE ( order_id , movie_id ) = %s ; "
        query_params = ( quantity , )

        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
        script.flashMessage(crud='update')

        return redirect('/employees')

@views_order_items.route( "/delete_order_item/<int:id>" , methods = [ "GET" , "POST" ] )
def delete_order_item( id ) :
    query = "DELETE FROM Order_items WHERE ( order_id , movie_id  ) = '%s';"
    db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    time.sleep(1)
    return redirect("/order_items")

pass