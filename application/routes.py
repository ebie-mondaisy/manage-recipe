#assistance with dashboard layout from - https://csveda.com/library-management-system-with-flask-and-postgresql/
import re
from application import db, app
from flask import Flask, render_template, jsonify, request, redirect, flash, Markup, url_for, session
from models import *
from forms import *
from datetime import date, timedelta

#creating routes for the main site - in this routes folder, i will combine parts to make a dashboard
@app.route('/home')
def home():


    return render_template('home.html')

@app.route('/create')
def create():
    pass

# @app.route("/logout")
# def logout():
#     return render_template("index.html")

# @app.route("/new_user", methods=['GET', 'POST'])
# def new_user():
#     form = LoginForm()

#     if form.validate_on_submit():
#         foodie = foodieList(foodiename=form.foodieName.data)
#         pwd = foodieList(password=form.password.data)
#         db.session.add(foodie, pwd)
#         db.session.commit()
#         flash('Now registered!')
#         return redirect(url_for('login'))
#     return render_template('new_user.html', title='New User', form=form)

# @app.route("/login")
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#     fname = request.form.get("foodiename")
#     pwd = request.form.get("password")
#     flist = foodieList.query.filter_by(foodieName=form.foodieName.data).first()
#     session['foodieName']= fname
#     session['foodieID']= flist.foodieID
#     if flist.password==pwd:
#         return render_template("home.html")
#     else:
#         return render_template("index.html")