import os
import secrets
from flask import render_template, url_for, flash, redirect, request, abort
from search import app, db, bcrypt
from search.forms import Search, AddUser, Contact
from search.models import Users

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/new", methods=['GET', 'POST'])
def new():
	form = AddUser()
	if form.validate_on_submit():
		user = Users(username=form.username.data, firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('register.html', form=form)


@app.route("/search", methods=['GET', 'POST'])
def search():
	form = Search()
	return render_template('search.html', form=form)

@app.route("/details", methods=['GET', 'POST'])
def details():
	form = Search()
	user = Users.query.filter_by(username=form.searchterm.data).first()
	if not user:
		return redirect(url_for('search'))
	return render_template('details.html', user=user)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
	form = Contact()
	if form.validate_on_submit():
		return redirect(url_for('success'))
	return render_template('contact.html', form=form)

@app.route("/success")
def success():
	return render_template('success.html')
