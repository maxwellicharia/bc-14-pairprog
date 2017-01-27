from flask import Flask, render_template, request, redirect, url_for, abort, session

from app import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	
	user = Users()
    
	if form.validate_on_submit():
        
		user = Users(email=form.email.data,
                    username=form.username.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.password.data)

        # Adds a new user to the database

        db.session.add(user)
        
        db.session.commit()
        
        # redirect to the login page
        
        return redirect(url_for('auth.login'))

	return render_template('auth/login.html', form=form, title='Register')
	
# If user has signed up login immediately
# Implement user login to store to database