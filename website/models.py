from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note (db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key is unique
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func.now() is a function that gets the current time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user.id is the table name
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key is unique
    email = db.Column(db.String(150), unique=True) # unique is unique
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # this is a relationship between the user and the note table