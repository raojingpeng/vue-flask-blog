# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'No one can hide from my sight')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


config = {
    'development': DevelopmentConfig
}



