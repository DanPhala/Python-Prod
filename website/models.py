#creating the database models for our users and notes
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    #associating the notes with each user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   #one-to-many relationship that is why is stored in the child object

class User(db.Model, UserMixin):
    #defining all the column
    id = db.Column(db.Integer , primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #for all users to be able to find theirs notes
    notes = db.relationship('Note')