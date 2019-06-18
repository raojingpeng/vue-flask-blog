# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
import os
import click
from flask import Flask

from blog.extensions import db, migrate
from blog.config import config
from blog.fake import fake_posts
from blog.api import api_bp
from blog.models import User, Post


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blog')
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_extensions(app)
    register_shell_context(app)
    register_commands(app)

    return app


def register_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, Post=Post)


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database"""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialize database.')

    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True,
                  help='The password used to login.')
    def adduser(username, password):
        """Create blog user"""
        user = User.query.filter_by(username=username).first()
        if user is not None:
            click.echo('The user already exists, updating...')
        else:
            click.echo('Creating user...')
            user = User(username=username)

        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo('Done.')

    @app.cli.command()
    @click.option('--post', default=50, help='Quantity of posts, default is 50.')
    def forge(post):
        """Generate fake data."""
        click.echo('Generating %d posts...' % post)
        fake_posts(post)




