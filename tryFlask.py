from flask import Flask
from tryFlask import sqlalchemy

# setting up the configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instantiate a database
db = sqlalchemy(app)

db.create_all()