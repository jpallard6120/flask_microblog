from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, DataRequired

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[InputRequired()])
    password = PasswordField(label='Password', validators=[InputRequired()])
    remember_me = BooleanField(label='Remember Me')
    submit = SubmitField(label='Sign In')