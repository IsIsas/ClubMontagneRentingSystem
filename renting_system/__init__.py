from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate


def create_app():

    f_app = Flask("RentingSystem", template_folder="templates", static_folder="static")
    f_app.config.from_pyfile('config.py')
    f_app.config['JSON_SORT_KEYS'] = False
    Bootstrap(f_app)

    return f_app

app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

