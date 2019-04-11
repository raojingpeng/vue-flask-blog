# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
import os
from flask import Flask

from blog.extensions import db, migrate
from blog.config import config
from blog.api import api_bp
from blog.models import User


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blog')
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_extensions(app)
    register_shell_context(app)

    return app


def register_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User)


