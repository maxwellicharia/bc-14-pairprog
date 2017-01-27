from flask import render_template, url_for, flash, request

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

	# error = None
	# if request.method == 'POST':
	#     if request.form['username'] != app.config['USERNAME']:
	#         error = 'Invalid username'
	#     elif request.form['password'] != app.config['PASSWORD']:
	#         error = 'Invalid password'
	#     else:
	#         session['logged_in'] = True
	#         flash('You were logged in')
	#         return redirect(url_for('show_entries'))
	return render_template('login.html')



@app.route('/firebase')
def firebase():
	# refkey = 
		return render_template("firepad.html")

if __name__ == '__main__':
    app.run()