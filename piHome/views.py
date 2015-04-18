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

@app.route('/', methods=['GET'])
def index():
    return make_response(open('piHome/templates/index.html').read())

@app.route('/views/login', methods=['GET'])
def view_login():
    return make_response(open('piHome/templates/views/login.html').read())

@app.route('/views/home', methods=['GET'])
def view_home():
    return make_response(open('piHome/templates/views/home.html').read())

@app.route('/views/mngmnt', methods=['GET'])
def view_mgmt():
    return make_response(open('piHome/templates/views/mngmnt.html').read())


@app.route('/views/stats', methods=['GET'])
def view_stats():
    return make_response(open('piHome/templates/views/stats.html').read())

@app.route('/views/control', methods=['GET'])
def view_contrl():
    return make_response(open('piHome/templates/views/control.html').read())
