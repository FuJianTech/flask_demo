# !/bin/env python
# -*- coding=utf-8 -*-
from flask import jsonify
from . import application_test


@application_test.route("/test", methods=['GET'])
def test():
    return jsonify({"data": "test blueprint"})


