from flask import render_template

from flask_login import login_required

from .home import *



@home.route('/')
def home():
    """
    	Render the my main page
    	"""
    return render_template('base.html', title="Welcome")





    # Incorporate view-form structure, blueprint revert back to initial structure