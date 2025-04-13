from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import os

app = Flask(__name__)

# Load configuration from .env file
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = os.getenv('SESSION_KEY_PREFIX', 'default:')

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
Session(app)

# Import routes and models
from . import routes, models

# Create database tables
with app.app_context():
    db.create_all()