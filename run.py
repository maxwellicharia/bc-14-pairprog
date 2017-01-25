import os

from app import app, dev_app

from app import set_app

name = os.getenv('FLASK_CONFIG')
# Get the necessary OS environment
app = dev_app(config_name)

if __name__ == '__main__':
    app.run()