# !/bin/env python
# -*- coding=utf-8 -*-
import configparser
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
appdir = basedir = os.path.abspath(os.path.dirname(__file__))

big_config = f"{appdir}{os.sep}etc{os.sep}config.cfg"  # /apps/etc/config.cfg


def little_config():
    """
    read /apps/etc/test/config.cfg
    :return: dict
    example:
        {'project_port': '5021',
        'blueprint_set': {'application_test': 'apps.logic.applications.application_test',
                        'application_example': 'apps.logic.applications.application_example'}}
    """
    config = configparser.ConfigParser()
    config.read(big_config, encoding="utf-8-sig")

    # 小配置 /apps/etc/test/config.cfg
    config_sections = config._sections
    project_name = get_config_value_by_key(config_sections, "current_project", "project_name")
    little_config = f"{appdir}{os.sep}etc{os.sep}{project_name}{os.sep}config.cfg"
    config.read(little_config, encoding="utf-8-sig")

    project_port = get_config_value_by_key(config_sections, "basic_set", "port")
    blueprint_set = config_sections["blueprint_set"]
    project_dict = {"project_port": project_port, "blueprint_set": blueprint_set}

    return project_dict


def get_config_value_by_key(config_sections, node_key, key=None):
    node_dict = config_sections.get(node_key, {})
    return node_dict.get(key) if key else node_dict


