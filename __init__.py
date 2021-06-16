from flask import Flask
from .extensions import db
from .routes import short

def create_app(config_file="settings.py"):
    app= Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(short)
    return app


# This is for only those who are using virtual-environment (in my case it's pipenv)
#start pipenv virtual environment before anything alse by
#   move to the root-most folder of the project
#   type in command prompt
#   pipenv shell
#   good to go

#creating database before first use
#   "set database path" $ export SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
#   "run python" $ python
#   inside python do the following :- 
#       >>>from URL_Shortner import create_app
#       >>>from URL_Shortner.extensions import db
#       >>>from URL_Shortner.models import Link
#       >>>db.create_all(app=create_app())
