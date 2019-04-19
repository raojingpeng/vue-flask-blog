# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
import jwt
import hashlib
from datetime import datetime, timedelta
from flask import url_for, current_app
from blog.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        pagination = query.paginate(page, per_page)
        data = {
            'items': [item.to_dict() for item in pagination.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': pagination.pages,
                'total_items': pagination.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if pagination.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if pagination.has_prev else None
            }
        }

        return data


class User(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_access = db.Column(db.DateTime(), default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_jwt(self, expires_in=600):
        now = datetime.utcnow()
        payload = {
            'user_id': self.id,
            'username': self.username,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }

        return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_jwt(token):
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm='HS256')
        except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidSignatureError) as e:
            return None

        return User.query.get(payload.get('user_id'))

    def gravatar(self, size):
        """返回gravatar头像"""
        digest = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def ping(self):
        self.last_access = datetime.utcnow()
        db.session.add(self)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'location': self.location,
            'about_me': self.about_me,
            'member_since': self.member_since.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'last_access': self.last_access.strftime('%Y-%m-%dT%H:%M:%SZ'),
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'gravatar': self.gravatar(128)
            }
        }
        if include_email:
            data['email'] = self.email

        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'name', 'location', 'about_me']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def __repr__(self):
        return '<User %s>' % self.username
