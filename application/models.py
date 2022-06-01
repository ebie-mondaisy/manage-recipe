from application import db
#models will include the tables needed to create and update recipes. An additional tale is created for users to review recipes 
#that they may have cooked

class Cuisines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisName = db.Column(db.String, nullable=False)

class makeRecipe(db.Model):
    id = db.Column(db.String, primary_key=True)
    recipeName = db.Column(db.String, nullable=False)
    CuisID = db.Column(db.Integer, db.ForeignKey("Cuisines.cuisID"), nullable=False)
    creatorName = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nulable=False)
    instructions = db.Column(db.String, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String, nullable=False)
    recipe_notes = db.relationship("trackCook", cascade="all, delete, delete-orphan", backref="recipe", lazy=True)
    cuisine = db.relationship("Cuisines", backref="cuisine", lazy=True)

class trackCook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    RecNumber = db.Column(db.String, db.ForeignKey("makeRecipe.recipID"), nullable=False)
    madeDate = db.Column(db.Date, nullable=False)
    success = db.Column(db.String, nullable=False)
    enjoyRate = db.Column(db.Integer, nullable=False)
    notes = db.Colum(db.String, unique=False)