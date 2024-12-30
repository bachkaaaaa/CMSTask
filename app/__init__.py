# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Get the absolute path to the directory containing this file
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Configure the database path correctly
    DB_PATH = os.path.join(BASE_DIR, 'db', 'data.db')
    
    # Ensure the db directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database with the app
    db.init_app(app)
    
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    # Import and register blueprints
    try:
        from .routes import app as routes_blueprint
        app.register_blueprint(routes_blueprint)
    except ImportError as e:
        print(f"Error importing routes: {e}")
    
    return app