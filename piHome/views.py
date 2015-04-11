#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, g, session, request, flash, redirect, url_for, Response
from flask import send_file, make_response, abort, jsonify, send_from_directory
import os

from piHome import app
from piHome.config import APP_STATIC

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(APP_STATIC, 'imgs/favicon.ico')

@app.route('/',methods=['GET'])
def index():
    return make_response(open('piHome/templates/index.html').read())

@app.route('/views/login',methods=['GET'])
def view_login():
    return make_response(open('piHome/templates/views/login.html').read())