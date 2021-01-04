# !/bin/env python
# -*- coding=utf-8 -*-
from . import application_base_blueprint
from flask import render_template


@application_base_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
