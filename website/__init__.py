from flask import Flask, json, redirect
from flask_mysqldb import MySQL


def create_app():
    app = Flask(__name__)
    # Shouldn't share this, just a random string to keep things secure
    app.config['SECRET_KEY'] = 'asklnvkxqoznmcvoqe'
    # app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
    # app.config['MYSQL_USER'] = 'cs340_username'
    # app.config['MYSQL_PASSWORD'] = '####'
    # app.config['MYSQL_DB'] = 'cs340_username'
    # app.config['MYSQL_CURSORCLASS'] = "DictCursor"

    # register views
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    from .views_employees import views_employees
    app.register_blueprint(views_employees, url_prefix='/')
    from .views_actors import views_actors
    app.register_blueprint(views_actors, url_prefix='/')
    from .views_customers import views_customers
    app.register_blueprint(views_customers, url_prefix='/')
    from .views_movies import views_movies
    app.register_blueprint(views_movies, url_prefix='/')
    from .views_order_items import views_order_items
    app.register_blueprint(views_order_items, url_prefix='/')
    from .views_orders import views_orders
    app.register_blueprint(views_orders, url_prefix='/')
    from .views_performances import views_performances
    app.register_blueprint(views_performances, url_prefix='/')

    # Test access for development
    # DB login DELETE IN FINAL VERSION
    mysql = MySQL(app)
    @app.route('/test')
    def root():
        query = "SELECT * FROM diagnostic;"
        query1 = 'DROP TABLE IF EXISTS diagnostic;';
        query2 = 'CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);';
        query3 = 'INSERT INTO diagnostic (text) VALUES ("MySQL is working!")';
        query4 = 'SELECT * FROM diagnostic;';
        cur = mysql.connection.cursor()
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        cur.execute(query4)
        results = cur.fetchall()
        return "<h1>MySQL Results" + str(results[0])

    return app