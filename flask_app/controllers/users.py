from flask import render_template, redirect, request # import tools from flask
from flask_app import app # import intance of Flask named app in __init__.py
from flask_app.models.user import User # import the User class from models

@app.route('/users')
def read_all_users():
    # query database for all users
    users = User.get_all()
    return render_template('/read_all.html', users = users) # send users variable to html template

@app.route('/users/new') # loads the add new user page
def new_user():
    return render_template('create.html')

@app.route('/users/add', methods=['POST']) # processes form data without reposting it
def add_user():
    new_user = User.save(request.form) # initiate instance with form data
    return redirect('/users')