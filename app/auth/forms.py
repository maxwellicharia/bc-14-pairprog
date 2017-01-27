from flask_wtf import FlaskForm

# Flask forms for implementing login and signup

from wtforms import PasswordField, StringField, SubmitField, ValidationError

# Various fields for enabling input areas

from wtforms.validators import DataRequired, Email, EqualTo

# Validators to ensure proper input is given

from ..models import User

#To change employee

class SignUp(FlaskForm):
    """
        Signup form for the users to create a pairprogramming session account
        """
    first_name = StringField('First Name', validators=[DataRequired()])
    #Datarequired to ensure the user inputs the field
    last_name = StringField('Last Name', validators=[DataRequired()])
    
    username = StringField('UserName', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    #Equal to fields to ensure the user passwords are both correct
    confirm_password = PasswordField('Confirm Password')
    
    submit = SubmitField('Sign Up')

    def check_username_valid(self, field):
    # Function to check whether username is valid and has not been referenced anywhere in the database
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

    def check_email_valid(self, field):
    # Function to check whether the email has been taken by someone
        if User.query.filter_by(Email=field.data).first():
            raise ValidationError('Invalid password, try again.')

class Login(FlaskForm):
    """
        Users to log in to their account for pair programming
        """
    
    username = StringField('UserName', validators=[DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    submit = SubmitField('Login')