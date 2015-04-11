# -*- coding: utf-8 -*-
from datetime import timedelta
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
SECRET_KEY = 'development key'
DEBUG = True

JWT_EXPIRATION_DELTA = timedelta(seconds=3000)