from flask import current_app
from flask_login import AnonymousUserMixin, UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db, login_manager

class Datatest(db.Model):
    __tablename__ = 'datatest'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    d1 = db.Column(db.String(64))
    d2 = db.Column(db.String(64))
    d3 = db.Column(db.DateTime)
    d4 = db.Column(db.Float)
    # users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Datatest \'%s\'>' % self.name

