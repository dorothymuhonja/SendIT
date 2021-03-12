from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    parcels = db.relationship('Parcel', backref='sender', lazy='dynamic')
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        return AttributeError('You cannot read the password attribute')
    


    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def save_user(self):
        db.session.add(self)
        db.session.commit()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):

        return '<Role {}>'.format(self.is_admin)

class Parcel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(140))
    status = db.Column(db.String(20))
    location = db.Column(db.String(20))
    recipient = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def save_parcel(self):
        db.session.add(self)
        db.session.commit()

    def cancel_parcel(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_parcel(cls,id):
        parcels=Parcel.query.filter_by(user_id=id).all()
        return parcels

 
    def __repr__(self):
        return '<Parcel {}>'.format(self.details)

