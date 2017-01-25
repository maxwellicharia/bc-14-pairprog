import os

from app import dev_app

config_name = os.getenv("[FLASK_CONFIG]") or 'default'
# Get the necessary OS environment
app = dev_app(config_name)

if __name__ == '__main__':
    app.run()