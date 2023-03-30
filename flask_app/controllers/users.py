from flask import render_template, redirect, request # import tools from flask
from flask_app import app # import intance of Flask named app in __init__.py
from flask_app.models.user import User # import the User class from models

@app.route('/users')
def read_users():
    # query database for all users
    users = User.get_all()
    return render_template('/read.html', users = users) # send users variable to html template

@app.route('/users/<int:id>')
def show_user(id):
    user = User.get_one(id)
    return render_template('show.html', user=user)

@app.route('/users/new') # loads the add new user page
def new_user():
    return render_template('create.html')

@app.route('/users/add', methods=['POST']) # processes form data without reposting it
def add_user():
    new_user = User.save(request.form) # initiate instance with form data
    return redirect(f"/users/{new_user}")

@app.route('/users/<int:user_id>/edit') # route displays user edit form
def show_edit_user_form(user_id):
    user = User.get_one(user_id)
    return render_template('edit.html', user = user)

@app.route('/users/process_edit', methods=['POST']) # route sends update request to database
def edit_user():
    User.update(request.form) # sends query to update table record
    return redirect(f"/users/{request.form['id']}")

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.delete(user_id) # deletes row from database
    return redirect('/users')