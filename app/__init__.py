from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import app_config

app.config.from_object('config')

db = SQLAlchemy()

# Initialise a database variable

def dev_app(config_name):
# changed from create_app
# changed from config_name
    app = Flask(__name__, instance_relative_config=True)
    #ensure specified file is loaded from instance directory
    app.config.from_object(app_config[config_name])
    
    app.config.from_pyfile('config.py')
    
    db.init_app(app)

    return app


def set_app(config_name):
    # existing code remains

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app