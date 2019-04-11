# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
import re
from flask import request, jsonify, url_for
from blog import db
from blog.api import api_bp
from blog.api.errors import bad_request
from blog.models import User

"""
GET    /api/users	    返回所有用户的集合
POST   /api/users	    注册一个新用户
GET	   /api/users/<id>	返回一个用户
PUT	   /api/users/<id>	修改一个用户
DELETE /api/users/<id>	删除一个用户
"""


@api_bp.route('/users', methods=['Post'])
def create_user():
    """注册新用户"""
    data = request.get_json()
    if not data:
        return bad_request('Please post json data.')

    message = {}
    if 'username' not in data or not data['username']:
        message['username'] = 'Please provide a valid username.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.' \
              '[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data['email']):
        message['email'] = 'Please provide a valid email.'
    if 'password' not in data or not data['password']:
        message['password'] = 'Please provide a valid password.'

    if User.query.filter_by(username=data['username']).first():
        message['username'] = 'user with this username already exists.'
    if User.query.filter_by(email=data['email']).first():
        message['email'] = 'user with this email already exists.'
    if message:
        return bad_request(message)

    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)

    return response


@api_bp.route('/users', methods=['GET'])
def get_users():
    """返回所有用户的集合"""
    pass


@api_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """返回一个用户"""
    return jsonify(User.query.get_or_404(id).to_dict())


@api_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """修改一个用户"""
    pass


@api_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """删除一个用户"""
    pass
