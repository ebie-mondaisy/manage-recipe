from application import db
#models will include the tables needed to create users and give them table to use on the dashboard

# class foodieList(db.Model):
#     foodieID = db.Column(db.Integer, primary_key=True)
#     foodieName = db.Column(db.String, nullable=False)
#     password = db.Column(db.String, nullable=False)


# class Cuisines(db.Model):
#     cuisID = db.Column(db.Integer, primary_key=True)
#     cuisName = db.Column(db.String, nullable=False)

class makeRecipe(db.Model):
    recipID = db.Column(db.String, primary_key=True)
    recipeName = db.Column(db.String, nullable=False)
    #CuisID = db.Column(db.Integer, db.ForeignKey("Cuisines.cuisID"), nullable=False)
    creatorName = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nulable=False)
    instructions = db.Column(db.String, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String, nullable=False)
    recipe_notes = db.relationship("trackCook", cascade="all, delete, delete-orphan", backref="recipe", lazy=True)
    #cuisine = db.relationship("Cuisines", backref="cuisine", lazy=True)

class trackCook(db.Model):
    createID = db.Column(db.Integer, primary_key=True)
    RecNumber = db.Column(db.String, db.ForeignKey("makeRecipe.recipID"), nullable=False)
    #FoodieID = db.Column(db.Integer, db.ForeignKey("foodieList.foodieID"), nullable=False)
    madeDate = db.Column(db.Date, nullable=False)
    success = db.Column(db.String, nullable=False)
    enjoyRate = db.Column(db.Integer, nullable=False)
    notes = db.Colum(db.Text(), unique=False)
    #foodie = db.relationship("foodieList", backref="foodie", lazy=True)