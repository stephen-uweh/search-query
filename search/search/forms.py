from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email
from search.models import  Users

class AddUser(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	firstname = StringField('Firstname', validators=[DataRequired()])
	lastname = StringField('Lastname', validators=[DataRequired()])
	submit = SubmitField('Add User')

class Search(FlaskForm):
	searchterm = StringField('Enter username you want to search for', validators=[DataRequired()])
	search = SubmitField('Search')

class Contact(FlaskForm):
	firstname = StringField('Firstname', validators=[DataRequired()])
	lastname = StringField('Lastname', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	message = TextAreaField('Send a message', validators=[DataRequired()])
	submit = SubmitField('Send')