#!/usr/bin/env python3
# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3,24)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('Repeat password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remeber_me = BooleanField('Remeber me')
    submit = SubmitField('Submit')


