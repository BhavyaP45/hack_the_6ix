#Import modules and libraries that will be used throughout the different files
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask_wtf import FlaskForm
import sqlite3

#Create app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db' #Configure a DB using SQLite
app.config['SECRET_KEY'] = 'e5c9095100a0ab1d7cb9a75f' #Configure a security key to ensure a secure connection

#Create a database model
db = SQLAlchemy()
db.init_app(app)

#Bcrypt class to store hashed passwords
bcrypt = Bcrypt(app)

#Use flask_login built in login class for users
loginmanager = LoginManager(app)
loginmanager.login_view = "login_page" #When unauthorized user tries clicking the market button, gets redirected

#Obtain routes from routes.py in the docs module
from docs import routes