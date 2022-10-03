"""This package handles setting up and providing the database connection."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////api/gpa_calculator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create database instance
db = SQLAlchemy(app)
