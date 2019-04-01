# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
import os
from flask import Flask
from blog.config import config
from blog.blueprints.api import api_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blog')
    app.config.from_object(config[config_name])

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')
