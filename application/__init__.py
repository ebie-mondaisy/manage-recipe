from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#setting up the database. creating credentials for the database and the forms to be created
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

from application import routes