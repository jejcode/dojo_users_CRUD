# Coding Dojo Assignment: Users CR

Create an app that displays all records from a database table, with a route to add a new row to that table.

What I learned:
More bootstrap formatting options
Once the full folder structure is in place, import needs a path name. For example, to import a controlller class:
    from flask_app.controllers.users import User

import structure:
__init__.py
    --from flask import Flask
    --create instance of Flask (app = Flask(__name__))
server.py
    --import instance of Flask (from flask_app import app)
    --import controller (from flask_app.controllers import controller.py)
each model
    --import db model (from flask_app.config.mysqlconnection.py import connectToMySQL)
each controller
    --from flask import render_template, redirect, request
    --from flask_app import app
    --from flask_app.models.user import User