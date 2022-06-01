from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, TextAreaField, PasswordField, SelectField, DateField
from wtforms.validators import DataRequired, ValidationError, ValidateUsername, InputRequired, Length, NumberRange
from models import *

#create forms to add, update and delete books.
class CreateCuisine(FlaskForm):
    cuisName = StringField('Cuisine:', validators=[Length(min=1, max=30), DataRequired()], render_kw={"placholder": "Cuisine"})
    submit = SubmitField("Add Cuisine")

class CreateRecipe(FlaskForm):
    recipeName = StringField('Recipe Name:', validators=[Length(min=1, max=80), DataRequired()], render_kw={"placeholder": "Recipe Name"})
    creatorName = StringField('Foodie Name:', validators=[Length(min=1, max=30), DataRequired()], render_kw={"placeholder": "Cook's Name"})
    cuisName = SelectField('Select Cuisine:', choices=[], validators=[DataRequired()])
    description = TextAreaField('Description:', validators=[Length(min=1, max=300)], render_kw={"placeholder": "Recipe Description"})
    ingredients = TextAreaField('Recipe Ingredients:', validators=[DataRequired()], render_kw={"placeholder": "Recipe Ingredients"})
    instructions = TextAreaField('Recipe Instructions:', validators=[DataRequired()], render_kw={"placeholder": "Recipe Instructions"})
    calories = IntegerField('Calorie Content:', validators=[InputRequired()], render_kw={"placeholder": "Recipe Calorie Content"})
    difficulty = SelectField('Recipe Difficulty:', choices=[("easy", "Easy".capitalize()), ("intermediate", "Intermediate".capitalize()), ("advanced", "Advanced".capitalize())])
    submit = SubmitField("Add Recipe")

class RecipeTrack(FlaskForm):
    recipeName = SelectField('Recipe Name:', choices=[], validators=[DataRequired()])
    madeDate = DateField('Date recipe was cooked:', format='%d-%m-%Y')
    success = SelectField('Success of recipe:', choices=[("could have done better", "Could have done better".capitalize()), ("satisfactory", "Satisfactory".capitalize()), ("cooked to perfection", "Cooked to perfection".capitalize())])
    enjoyRate = IntegerField('Enjoyment rating:', validators=[NumberRange(min=1, max=10), InputRequired()])
    notes = TextAreaField('Recipe notes:', validators=None)
    add_tracking = SubmitField("Add Recipe Review")

class UpdateRecipe(FlaskForm):
    recipeName = StringField("Recipe Name:", validators=[Length(min=1, max=80), DataRequired()])
    creatorName = StringField('Foodie Name:', validators=[Length(min=1, max=30), DataRequired()])
    cuisName = SelectField('Select Cuisine:', choices=[], validators=[DataRequired()])
    description = TextAreaField('Description:', validators=[Length(min=1, max=300)])
    ingredients = TextAreaField('Recipe Ingredients:', validators=[DataRequired()])
    instructions = TextAreaField('Recipe Instructions:', validators=[DataRequired()])
    calories = IntegerField('Calorie Content:', validators=[InputRequired()])
    difficulty = SelectField('Recipe Difficulty:', choices=[("easy", "Easy".capitalize()), ("intermediate", "Intermediate".capitalize()), ("advanced", "Advanced".capitalize())])
    update = SubmitField("Update Recipe")

class UpdateCuisine(FlaskForm):
    cuisName = StringField('Cuisine:', validators=[Length(min=1, max=30), DataRequired()])
    update_c = SubmitField("Update Cuisine")