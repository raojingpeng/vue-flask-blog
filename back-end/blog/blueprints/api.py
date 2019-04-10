# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask import Blueprint, jsonify
from flask_cors import CORS

api_bp = Blueprint('api', __name__)
CORS(api_bp)


@api_bp.route('/ping')
def ping():
    """测试api是否连通"""
    return jsonify('Yes!')
