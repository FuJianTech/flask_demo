# !/bin/env python
# -*- coding=utf-8 -*-

import os
import time
from flask import Flask
from apps import appdir, little_config


def create_app():
    """
    :return: <class 'flask.app.Flask'>
    """
    app = Flask(__name__,
                static_folder=appdir + os.sep + 'static',
                template_folder=appdir + os.sep + 'templates'
                )
    register_blueprint(app)

    return app


def register_blueprint(app):
    """
    __import__('os',globals(),locals(),['path','pip'])  # == from os import path, pip
    base  blueprint register
    :param app:   from  Flask(__name__)
    :return: None
    """

    from apps.logic.applications.application_base_blueprint import application_base_blueprint
    app.register_blueprint(application_base_blueprint)
    blueprint_info_list = little_config()["blueprint_set"]
    all_time = 0
    for key, value in blueprint_info_list.items():
        t1 = time.time()
        blueprint_name, model_path = key, value
        # blueprint modular
        module_instance = __import__(model_path, globals(), locals(), [blueprint_name])
        all_time += (time.time() - t1)
        print(f'{blueprint_name} spend_time : {time.time() - t1}')
        try:
            blueprint_model = getattr(module_instance, blueprint_name)
        except BaseException as e:
            blueprint_model = getattr(eval(blueprint_name), blueprint_name)

        app.register_blueprint(blueprint_model)

    print(f'all_spend_time : {all_time}')
