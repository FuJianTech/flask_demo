# !/bin/env python
# -*- coding=utf-8 -*-
# This is a basic blueprint and will always be registered
# from . import views  Should be placed last


from flask import Blueprint
application_base_blueprint = Blueprint('application_base_blueprint', __name__)

from. import views
