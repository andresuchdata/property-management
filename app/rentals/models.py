# Rental models

import uuid
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db


class Rental(db.Model):
    __tablename__ = 'rentals'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    total_price = db.Column(db.Float, nullable=False)
    period = db.Column(db.Integer, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    property = db.relationship('Property', backref='rentals')
    user = db.relationship('User', backref='rentals')
    payment = db.relationship('Payment', uselist=False, back_populates='rental')

    @classmethod
    def get_all_with_details(cls):
        return cls.query.options(db.joinedload('property'), db.joinedload('user')).all()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, rental_id):
        return cls.query.get(rental_id)

    @classmethod
    def create(cls, data):
        new_rental = cls(**data)
        try:
            db.session.add(new_rental)
            db.session.commit()
            return new_rental
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
            'total_price': self.total_price,
            'period': self.period,
            'property_id': self.property_id,
            'user_id': self.user_id
        }

    def __repr__(self):
        return f'<Rental {self.id}>'
