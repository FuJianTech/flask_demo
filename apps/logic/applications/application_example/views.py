# !/bin/env python
# -*- coding=utf-8 -*-
from flask import jsonify
from . import application_example


@application_example.route("/example", methods=['GET'])
def example():
    return jsonify({"data": "example blueprint"})
