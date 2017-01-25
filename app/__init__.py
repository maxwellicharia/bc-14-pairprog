from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

from config import app_config

from app import views

from flask_login import LoginManager

db = SQLAlchemy()
# Initialise a database variable
login_manager = LoginManager()


def dev_app(config_name):
	"""
		Function to start the app and initialise key variables
		"""
	app = Flask(__name__, instance_relative_config=True)
	#ensure specified file is loaded from instance directory
	app.config.from_object(app_config[config_name])
	#reference to the app_config object
	app.config.from_pyfile('config.py')
    
	db.init_app(app)
	# Use login manager to simplify login access to users
	login_manager.init_app(app)

	login_manager.login_message = "You must login to view page."

	login_manager.login_view = "auth.login"

	@app.route('/')
	def index():
		return render_template("index.html")

	return app