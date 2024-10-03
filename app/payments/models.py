# Payment models

import uuid
import enum
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db

class Currency(enum.Enum):
    IDR = 'idr'
    USD = 'usd'

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.Enum(Currency), nullable=False)
    payment_status = db.Column(db.Boolean, default=False, nullable=False)
    rental_id = db.Column(db.String(36), db.ForeignKey('rentals.id'), nullable=False)
    
    # Fields to be populated by external payment service
    transaction_id = db.Column(db.String(100))
    payment_method = db.Column(db.String(50))
    payment_date = db.Column(db.DateTime)

    rental = db.relationship('Rental', back_populates='payment')

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, payment_id):
        return cls.query.get(payment_id)

    @classmethod
    def create(cls, data):
        new_payment = cls(**data)
        try:
            db.session.add(new_payment)
            db.session.commit()
            return new_payment
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
            'amount': self.amount,
            'currency': self.currency.value,
            'payment_status': self.payment_status,
            'rental_id': self.rental_id,
            'transaction_id': self.transaction_id,
            'payment_method': self.payment_method,
            'payment_date': str(self.payment_date) if self.payment_date else None
        }

    def __repr__(self):
        return f'<Payment {self.id}>'
