# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask import g, jsonify
from blog.api import api_bp
from blog.api.auth import basic_auth


@api_bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_jwt()
    return jsonify({'token': token})
