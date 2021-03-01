from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from .models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PasswordUpdateForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(),EqualTo(new_password)])
    submit = SubmitField('Update Password')


class ApplyJobForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    job_id = StringField('Job ID', validators=[DataRequired()])
    apply_date = DateField()
    cv_upload = FileField()