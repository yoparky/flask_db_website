import time
from flask import Blueprint, redirect, render_template, flash, request
from .database import db_connector as db
from .database import db_reset

# All views here
views = Blueprint('views', __name__)
# connect to database
db_connection = db.connect_to_database()

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/reset_wait')
def reset_db():
    return render_template('reset_wait.html')

@views.route('/reset_db')
def reset_wait():
    for query in db_reset.reset_query:
        db.execute_query(db_connection=db_connection, query=query)
    return redirect('/')

