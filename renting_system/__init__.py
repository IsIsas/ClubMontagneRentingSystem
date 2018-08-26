from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap



# db variable initialization
db = SQLAlchemy()


def create_app():
    app = Flask("RentingSystem", template_folder="../build", static_folder="../build")
    app.config.from_pyfile('config.py')
    db.init_app(app)

    Bootstrap(app)

    return app
