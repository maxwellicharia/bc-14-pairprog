from flask import render_template, request, redirect, url_for, abort, session

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup', methods=['POST'])
def signup():
	if 
# If user has signed up login immediately

@app.route('/login', methods=['POST'])
def login():
	pass