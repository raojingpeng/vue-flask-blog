# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from blog.models import User
from blog.api.errors import error_response

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    """检查提供的用户名与密码"""
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user

    return user.check_password(password)


@token_auth.verify_token
def verify_token(token):
    """检查用户请求是否有token，并且token真实存在，还在有效期内"""
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None


@basic_auth.error_handler
def basic_auth_error():
    """认证失败，返回错误相应"""
    return error_response(401)


@token_auth.error_handler
def token_auth_error():
    """Token认证失败，返回错误相应"""
    return error_response(401)
