# -*- coding: utf-8 -*-
from datetime import timedelta
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
SECRET_KEY = 'development key'
DEBUG = True
DB_USER = 'pihome'
DB_PASS = 'pihome'
DB_NAME = 'pihome'

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@192.168.0.100/{}'.format(DB_USER,DB_PASS,DB_NAME)
SQLALCHEMY_ECHO = True

JWT_EXPIRATION_DELTA = timedelta(seconds=3000)