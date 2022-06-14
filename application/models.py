from application import db
#models will include the tables needed to create and update recipes. An additional tale is created for users to review recipes 
#that they may have cooked

class Cuisines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisName = db.Column(db.String(30), nullable=False)
    cuisine = db.relationship("makeRecipe", backref="cuisine", lazy=True)

class makeRecipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipeName = db.Column(db.String(100), nullable=False)
    creatorName = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    instructions = db.Column(db.String(1500), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(30), nullable=False)
    CuisID = db.Column(db.Integer, db.ForeignKey("cuisines.id"), nullable=False)
    recipe_notes = db.relationship("trackCook", backref="recipe", lazy=True)
    

class trackCook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    madeDate = db.Column(db.Date, nullable=False)
    success = db.Column(db.String(30), nullable=False)
    enjoyRate = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(600), unique=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("make_recipe.id"), nullable=False)