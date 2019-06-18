# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask import request, jsonify, url_for, g
from blog.api import api_bp
from blog.api.auth import token_auth
from blog.api.errors import error_response, bad_request
from blog.extensions import db
from blog.models import User, Post

"""
GET	   /api/posts	    返回所有文章的集合
POST   /api/posts	    添加一篇新文章
GET	   /api/posts/<id>  返回一篇文章
PUT	   /api/posts/<id>  修改一篇文章
DELETE /api/posts/<id>  删除一篇文章
"""


@api_bp.route('/posts', methods=['POST'])
@token_auth.login_required
def create_post():
    """添加一篇新文章"""
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    message = {}
    if 'title' not in data or not data['title']:
        message['title'] = 'Title is required.'
    elif len(data.get('title')) > 255:
        message['title'] = 'Title must less than 255 characters.'
    if 'body' not in data or not data['body']:
        message['body'] = 'Body is required.'
    if message:
        return bad_request(message)

    post = Post()
    post.from_dict(data)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('api.get_post', id=post.id)
    return response


@api_bp.route('/posts', methods=['GET'])
def get_posts():
    """返回文章集合，分页"""
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Post.to_collection_dict(Post.query.order_by(Post.timestamp.desc()), page, per_page, 'api.get_posts')
    return jsonify(data)


@api_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    """返回一篇文章"""
    post = Post.query.get_or_404(id)
    post.views += 1
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict())


@api_bp.route('/posts/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_post(id):
    """修改一篇文章"""
    post = Post.query.get_or_404(id)
    if g.current_user != post.author:
        return error_response(403)

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data')
    message = {}
    if 'title' not in data or not data['title']:
        message['title'] = 'Title is required.'
    elif len(data.get('title')) > 255:
        message['title'] = 'Title must less than 255 characters.'
    if 'body' not in data or not data['body']:
        message['body'] = 'Body is required.'
    if message:
        return bad_request(message)

    post.from_dict(data)
    db.session.commit()
    return jsonify(post.to_dict())


@api_bp.route('/posts/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_post(id):
    """删除一篇文章"""
    post = Post.query.get_or_404(id)
    if g.current_user != post.author:
        return error_response(403)
    db.session.delete(post)
    db.session.commit()
    return '', 204