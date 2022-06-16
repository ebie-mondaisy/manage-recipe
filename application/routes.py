import re
from application import db, app
from flask import Flask, render_template, jsonify, request, redirect, flash, Markup, url_for, session
from application.models import *
from application.forms import *
from datetime import date, timedelta

#creating routes for recipe management site
@app.route("/", methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    recipes = makeRecipe.query.all()
    return render_template('home.html', title = "Recipe Management - View", recipes=recipes)

@app.route('/create', methods=["GET", "POST"])
def create():
    form = CreateRecipe()

    cuisines = Cuisines.query.all()

    for cuisine in cuisines:
        form.cuisName.choices.append(
            (cuisine.id, f"{cuisine.cuisName}")
        )
    

    if request.method == "POST":

        print(form.cuisName.data)
        recipe = makeRecipe(recipeName = form.recipeName.data, creatorName = form.creatorName.data,
                            CuisID = form.cuisName.data , description = form.description.data, 
                            ingredients = form.ingredients.data, 
                            instructions = form.instructions.data, 
                            calories = form.calories.data, difficulty = form.difficulty.data)

        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfuly :)', 'success')
        return redirect(url_for('create'))
    return render_template("create.html", title = "Create Recipes Here!", form = form)

@app.route('/cuisine/create', methods=["GET", "POST"])
def create_cuisine():
    form = CreateCuisine()

    if form.validate_on_submit():

        cuisine = Cuisines(cuisName = form.cuisName.data)

        db.session.add(cuisine)
        db.session.commit()
        flash('Cuisine added successfully :)', 'success')
    return render_template("cuisine.html", title = "Add a Cuisine!", form = form)

@app.route('/cuisine')
def cuisine_view():
    all_cuisines =  Cuisines.query.all()
    return render_template("cuisine_list.html", title = "Cuisine List", all_cuisines=all_cuisines)

@app.route('/home/delete/<int:id>', methods = ['POST'])
def delete(id):
    db.session.delete(makeRecipe.query.get(id))
    db.session.commit()
    flash('You have deleted this recipe.', 'success')
    return redirect(url_for('home'))

@app.route("/search", methods=["POST"])
def search_recipe():
    recipe_search = makeRecipe.query.filter(makeRecipe.recipeName.like("%" + request.form["recipe_name"] + "%")).first()

    if recipe_search != None:
        return redirect(url_for('edit_recipe', id = recipe_search.id))
    else:
        flash('Recipe does not exist :(', 'danger')
        return redirect(url_for('home'))

@app.route("/home/edit/<id>", methods=["GET", "POST"])
def edit_recipe(id):
    look_recipe = makeRecipe.query.get_or_404(id)
    look_notes = trackCook.query.filter(trackCook.recipe_id == id).all()

    form_update =  UpdateRecipe(obj = look_recipe)
    add_track = RecipeTrack()

    if  form_update.update.data: #and form_update.validate_on_submit():
        look_recipe.recipeName = form_update.recipeName.data
        look_recipe.creatorName = form_update.creatorName.data
        look_recipe.description = form_update.description.data
        look_recipe.ingredients = form_update.ingredients.data
        look_recipe.instructions = form_update.instructions.data
        look_recipe.calories = form_update.calories.data
        look_recipe.difficulty = form_update.difficulty.data
        db.session.commit()
        flash('Recipe updated :)', 'success')
        return redirect(url_for('edit_recipe', id = look_recipe.id))

    if add_track.add_tracking.data:
        track = trackCook(madeDate = add_track.madeDate.data,
                            success = add_track.success.data, enjoyRate = add_track.enjoyRate.data, notes = add_track.notes.data, recipe_id = id)
        db.session.add(track)
        db.session.commit()
        flash('You have successfully added a note.', 'success')
        return redirect(url_for('edit_recipe', id = look_recipe.id))

    if request.method == "GET":
        return render_template("edit.html", title = "Edit Recipe!", recipe = look_recipe, recipe_notes = look_notes,
                                    form_update = form_update, add_track = add_track)

    return render_template("edit.html", title = "Edit Recipe!", recipe = look_recipe, recipe_notes = look_notes,
                                    form_update = form_update, add_track = add_track)

@app.route("/home/edit/track/<int:id>", methods = ["POST"])
def delete_track(id):
    #track_delete = trackCook.query.get_or_404(request.form['recipe_id'])
    db.session.delete(trackCook.query.get(id))
    db.session.commit()
    flash('Note deleted :)', 'success')
    return redirect(url_for('home'))