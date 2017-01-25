from flask_wtf import FlaskForm

from wtforms import PasswordField, StringField, SubmitField, ValidationError

from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee
#To change employee
class SignUp(FlaskForm):
    """
        Signup form for the users to create a pairprogramming session account
        """
    first_name = StringField('First Name', validators=[DataRequired()])
    
    last_name = StringField('Last Name', validators=[DataRequired()])
    
    username = StringField('UserName', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    
    submit = SubmitField('Sign Up')

    def check_email_valid(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def check_username_valid(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

class Login(FlaskForm):
    """
        Users to log in to their account for pair programming
        """
    
    username = StringField('UserName', validators=[DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    submit = SubmitField('Login')