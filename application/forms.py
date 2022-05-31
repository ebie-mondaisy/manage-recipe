from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, ValidationError, ValidateUsername, InputRequired
from models import *

#create forms to add, update and delete books.
# class LoginForm(FlaskForm):
#     foodieName = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Sign Up')

#     def validate_foodiename(self, foodieName):
#         foodie = foodieList.query.filter_by(foodieName=foodieName.data).first()
#         if foodie is not None:
#             raise ValidationError('Name in use. Please use another.')

#     def validate_password(self, password):
#         pwd = foodieList.query.filter_by(password=password.data).first()
#         if pwd is not None:
#             raise ValidationError('Password is not unique. Please create another.')

class CreateRecipe(FlaskForm):
    recipeName = StringField('Recipe Name:', validators=[DataRequired()])
    creatorName = StringField('Foodie Name:', validators=[DataRequired()])
    ingredients = TextAreaField('Recipe Ingredients:', validators=[DataRequired()])
    instructions = TextAreaField('Recipe Instructions:', validators=[DataRequired()])
    calories = IntegerField('Calorie Content:', validators=[DataRequired()])
    difficulty = SelectField('Recipe Difficulty:', choices=[("easy", "Easy"), ("intermediate", "Intermediate"), ("advanced", "Advanced")])
    submit = SubmitField("Add Recipe")
