from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up the configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instantiate a database
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()