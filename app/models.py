from datetime import datetime
from app import db
​
​
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    parcels = db.relationship('Parcel', backref='sender', lazy='dynamic')
    role_id = db.Column(db.integer, db.ForeignKey('role.id'))
​
    def __repr__(self):
        return '<User {}>'.format(self.username)
​
​
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    users = db.relationship('User', backref='role', lazy="dynamic")
​
​
class Parcel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(140))
    status = db.Column(db.String(20))
    location = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
​
    def __repr__(self):
        return '<Post {}>'.format(self.body)

