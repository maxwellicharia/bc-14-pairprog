class Config(object):
    """
    Common configurations that cut across to all environnents
        """
    GOOGLE_LOGIN_CLIENT_ID = "<your-id-ending-with>.apps.googleusercontent.com"
    GOOGLE_LOGIN_CLIENT_SECRET = "<your-secret>"
    OAUTH_CREDENTIALS={
        'google': {
            'id': GOOGLE_LOGIN_CLIENT_ID,
            'secret': GOOGLE_LOGIN_CLIENT_SECRET
        }
}

class DevConfig(Config):
    """
    Configurations set for the user to use and implement assistive toola
        """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    # Assist debugging errors that may arise

class ProdConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    #   Ensures that during deployments debug features are off for end user

app_config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig
}

#Creating a variable to access both elements of the class