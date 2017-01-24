from flask import render_template, request, redirect, url_for, abort, session

from app import app

login_manager = LoginManager()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup', methods=['POST'])
def signup():
	session['signup'] = request.form['signup']
    	return redirect(url_for('signup'))
	return render_template("signup.html")

# If user has signed up login immediately

@app.route('/login', methods=['POST'])
def login():
	