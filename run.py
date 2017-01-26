from flask import render_template, url_for, flash

import requests

import os

from app import dev_app

# from templates import *

from app.home.forms import *

config_name = os.getenv("[FLASK_CONFIG]") or 'default'

# Get the necessary application environment for use

app = dev_app(config_name)

app.secret_key = os.urandom(15)

@app.route('/')
def index():
	# The root and main page of the website
    return render_template("base.html")

@app.route('/login', methods=['POST', 'GET'])
def Login():

	form = LoginForm()

	if form.validate() == False:
	 	flash('All fields are required.')
		return render_template('login.html', form = form)
	elif request.method == 'GET':
		return render_template('contact.html', form = form)
	else:
		return render_template('success.html')
   	
   	return render_template('login.html', form = form)



@app.route('/firebase')
def firebase():
	# refkey = 
		render_template("firepad.html")

if __name__ == '__main__':
    app.run()