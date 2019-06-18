# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask import Blueprint
from flask_cors import CORS

api_bp = Blueprint('api', __name__)
CORS(api_bp)

# 防止循环导入
from blog.api import ping, users, posts, tokens
