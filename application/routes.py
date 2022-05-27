#assistance with dashboard layout from - https://csveda.com/library-management-system-with-flask-and-postgresql/
from application import db, app
from flask import Flask, render_template, jsonify, request, redirect, flash, Markup, url_for, session
from models import *
from datetime import date, timedelta

#creating routes for the main site - in this routes folder, i will combine parts to make a dashboard
@app.route('/')
def index():
    return render_template(index.html)

@app.route("/logout")
def logout():
    return render_template("index.html")

@app.route("/recipe-dashboard", methods=["POST"])
def recipe_dashboard():
    fnam = request.form.get("username")
    fpwd = request.form.get("password")
    flist = foodieList.query.filter_by(foodieName=fnam).first()
    session['foodieName'] = fnam
    session['foodieid'] = flist.foodieID
    session['ftype'] = flist.foodieType
    if flist.password==fpwd:
        return render_template("recipe-dashboard.html")
    else:
        return render_template("index.html")

#handling the recipe cuisines - create, add, update and delete
@app.route("/createCuisine", methods =["POST"])
def createCuisine():
    cName = request.form.get("cuisName")
    newCuis = Cuisines(cuisName=cName)
    db.session.add(newCuis)
    db.session.commit()
    conf = cName+' Successfully Created'
    return render_template("recipe-dashboard.html", conf=conf)

@app.route("/AddCuisine")
def AddCuisine():
    CuisList = Cuisines.query.all()
    table1 ='''<div class="form-group">
                <table class ="table table-bordered border-success" ><TR style="text-weight: bold; background-colour:##ccffe6;">
                <TD>Cuisine ID</TD>
                <TD>Cuisine Name</TD></TR>'''
    for item in CuisList:
        table1 = table1+"<TR><TD>"+str(item.cuisID)+"</TD><TD>"+item.cuisName+"</TD></TR>"
    table1 = table1+"</table></div>"
    string = '''<h5 style="text-align:center">Add a Cuisine</h5><HR>
    <form action="/createCuisine" method="post">
    <div class="row mb -3">
    <label for="cuisName" class="col-sm-2 col-form-label">Cuisine Name</label>
    <div class="col-sm-10">
        <input type="text" class="form-control" name="cuisName">
    </div>
    </div>
    <div class = "col-12>
        <button type="submit" class="btn btn-success mb-3">Add Cuisine</button>
    </div>
    
    </form>
    '''+table1
    txt= Markup(string)
    return render_template("recipe-dashboard.html", txt=txt)

#creating routes to allow the user to add recipes to their profile (database)
@app.route("/createRecipe", methos=["POST"])
def createRecipe():
    recID = request.form.get("recipID")
    rNam = request.form.get("recipeName")
    cID = int(request.form.get("cuisID"))
    crNam = request.form.get("creatorName")
    ing = request.form.get("ingredients")
    ins = request.form.get("instructions")
    cal = int(request.form.get("calories"))
    diff = request.form.get("difficulty")
    makRec = makeRecipe(recipID=recID, recipeName=rNam, cuisID=cID, creatorName=crNam, ingredients=ing, instructions=ins, calories=cal, difficulty=diff)
    db.session.add(makRec)
    db.session.commit()
    text = rNam+' recipe successfully saved'
    return render_template("recipe-dashboard.html", text=text)