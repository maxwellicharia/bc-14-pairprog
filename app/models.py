from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# To ensure security of users' info
from app import db, login_manager

class Users(UserMixin, db.Model):
    """
        User table for user signup info
        """
    # Retains plural of table names
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # Id for unique reference in the database
    email = db.Column(db.String(60), index=True, unique=True)
    # Limiting striing length and input to be unique
    username = db.Column(db.String(30), index=True, unique=True)
    # Ensure is unique
    first_name = db.Column(db.String(30), index=True)
    # Ensure is string
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(64))
    # limit password string length
    
    @property
    def password(self):
        """
            Password prevention from being seen
            """
        raise AttributeError('Password should not be seen.')
        # If tried to be seen attribute error is raised
    
    @password.setter
    def password(self, password):
        """
            Enable the password to be hashed
            """
        self.password_hash = generate_password_hash(password)

    def password_verify(self, password):
        """
            Check if both passwords match
            """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)
        # Formatting the user output


@login_manager.user_loader
# Set up user_loader to load the current users

def load_user(user_id):
    # Loads the users in
    return User.query.get(int(user_id))