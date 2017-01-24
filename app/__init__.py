from flask import Flask

app = Flask(__name__)

from app import views

app.config.from_object('config')
app.config['SECRET_KEY'] = '2356';
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://example.db'