#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-03 02:58:10
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-12 02:19:58
from flask import Flask

app = Flask(__name__)
app.config.from_object('piHome.config')

db = SQLAlchemy(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

import piHome.views