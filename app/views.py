from flask import Flask, render_template, request, redirect, url_for, abort, session

from app import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	pass
# If user has signed up login immediately

@app.route('/login', methods=['POST'])
def login():
	pass