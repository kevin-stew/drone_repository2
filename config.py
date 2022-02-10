import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# give us access to the project in ANY OS we find ourselves in
# allows outside files/folders to be added to the project from the directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set Config variables for the flask app.
    Using environment variables where available where otherwise
    create the config variable if not done already.
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_APP = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Random string here'
    SQLALCHEMY_DATABASE_URI =os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages from sql