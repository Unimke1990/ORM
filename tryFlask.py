from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid

# setting up the configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instantiate a database
db = SQLAlchemy(app)

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(30))

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username

user1 = User(name="Given Agim", email="aggiven@gmail.com", username="given9")


with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add(user1)
    db.session.commit()
    print("Database created and new user added successfully!")
    