from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[InputRequired()])
    password = PasswordField(label='Password', validators=[InputRequired()])
    remember_me = BooleanField(label='Remember Me')
    submit = SubmitField(label='Sign In')

class RegistrationForm(FlaskForm):
    username = StringField(label = 'Username', validators = [DataRequired()])
    email = StringField(label = 'Email', validators = [DataRequired(), Email()])
    password = PasswordField(label = 'Password', validators = [DataRequired()])
    password2 = PasswordField(
        label = 'Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField(label = 'Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField(label = 'Username', validators = [DataRequired()])
    about_me = TextAreaField(label = 'About Me', validators = [Length(min = 0, max = 140)])
    submit = SubmitField(label = 'Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')