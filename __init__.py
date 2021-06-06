from flask import Flask
from .extensions import db
from .routes import short

def create_app(config_file="settings.py"):
    app= Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(short)
    return app



#start pipenv virtual environment before anything alse by
#   move to the root-most folder of the project
#   type in command prompt
#   pipenv shell
#   good to go

#creating database before first use
#   from url_shortner import 