class Config(object):
    """
    Common configurations that cut across to all environnents
        """

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
    'prod': ProdConfig
}

#Creating a variable to access both elements of the class