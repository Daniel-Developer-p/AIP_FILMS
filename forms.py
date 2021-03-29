from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional, Email, EqualTo
from wtforms.widgets import TextArea, TextInput, PasswordInput, CheckboxInput


class ArticleForm(FlaskForm):
    img = StringField('Ссылка на картинку', widget=TextInput())
    title = StringField('Название статьи', validators=[DataRequired()])
    body = StringField('Содержание', validators=[DataRequired()], widget=TextArea())


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    remember_me = BooleanField('Запомнить меня', widget=CheckboxInput())


class RegisterForm(FlaskForm):
    name = StringField('Видимое имя на сайте', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    password_confirmation = StringField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')], widget=PasswordInput())
