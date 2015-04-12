#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-12 01:49:03
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-12 02:19:54
from flask.ext.sqlalchemy import SQLAlchemy

from passlib.apps import custom_app_context as pwd_context

from piHome import db
from piHome.config import APP_STATIC

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.password_hash = pwd_context.encrypt(kwargs.get('password'))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __str__(self):
        return str(self.username)


        