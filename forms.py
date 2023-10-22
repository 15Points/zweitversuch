from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, HiddenField, SelectField, StringField, SubmitField
from wtforms.validators import InputRequired, Length

class CreateTodoForm(FlaskForm):
    description = StringField(validators=[InputRequired(), Length(min=5)])
    submit = SubmitField('Create')

class TodoForm(FlaskForm):
    method = HiddenField()
    id = HiddenField()
    complete = BooleanField()
    description = StringField(validators=[InputRequired()])
    list_id = SelectField(coerce=int, choices=[], validate_choice=False)
    submit = SubmitField('Update')

class CreateListForm(FlaskForm):
    list_name = StringField(validators=[InputRequired(), Length(min=5)])
    submit = SubmitField('Create List')    

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
#from db import db
#
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min = 2, max = 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min = 4, max = 20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")
#
#    def validate_username(self, username):
#        existing_user_username = db.User.query.filter_by(
#            username = username.data).first()
#        if existing_user_username:
#            raise ValidationError(
#                "This username has already been taken. Please choose a different one."
#            )
#        
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min = 2, max = 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min = 4, max = 20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")