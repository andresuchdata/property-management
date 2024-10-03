# User models

import uuid
from sqlalchemy.dialects.mysql import BOOLEAN
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    nik = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    is_active = db.Column(BOOLEAN, default=False, nullable=False)
    profile_picture = db.Column(db.String(255))  # Store URL to Alibaba OSS
    password_hash = db.Column(db.String(255))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, )

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def create(cls, data):
        new_user = cls(**data)
        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except SQLAlchemyError:
            db.session.rollback()
            return None

    def update(self, data):
        try:
            for key, value in data.items():
                setattr(self, key, value)
            db.session.commit()
            return self
        except SQLAlchemyError:
            db.session.rollback()
            return None

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'nik': self.nik,
            'email': self.email,
            'phone': self.phone,
            'is_active': self.is_active,
            'profile_picture': self.profile_picture
        }

    def __repr__(self):
        return f'<User {self.email}>'
