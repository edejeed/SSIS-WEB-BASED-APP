from flask import Flask
from os import getenv
import cloudinary.uploader
from flask_mysqldb import MySQL

cloudinary.config(
    cloud_name = getenv('CLOUD_NAME'),
    api_key = getenv('API_KEY'),
    api_secret = getenv('API_SECRET')
)

mysql = MySQL() 

def create_app() -> object:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['MYSQL_HOST'] = getenv("DB_HOST")
    app.config['MYSQL_USER'] = getenv("DB_USERNAME")
    app.config['MYSQL_PASSWORD'] = getenv("DB_PASSWORD")
    app.config['MYSQL_DB'] = getenv("DB_NAME")
    mysql.init_app(app)

    # import blueprints
    from .views.students import student
    from .views.courses import course
    from .views.colleges import college


    # register blueprints
    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)

    return app

    