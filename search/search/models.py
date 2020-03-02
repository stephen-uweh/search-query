from datetime import datetime
from search import db


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	firstname = db.Column(db.String(120), nullable=False)
	lastname = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)