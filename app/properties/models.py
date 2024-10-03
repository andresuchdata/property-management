# Property models

import enum
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db

class UnitType(enum.Enum):
    LAND = 'land'
    HOUSE = 'house'
    ROOM = 'room'

class UnitPeriod(enum.Enum):
    MONTHS = 'months'
    DAYS = 'days'
    YEARS = 'years'

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unit_type = db.Column(db.Enum(UnitType), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    unit_period = db.Column(db.Enum(UnitPeriod), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    images = db.Column(db.JSON)  # Store URLs to Alibaba OSS

    def __repr__(self):
        return f'<Property {self.name}>'
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, property_id):
        return cls.query.get(property_id)

    @classmethod
    def create(cls, data):
        new_property = cls(**data)
        try:
            db.session.add(new_property)
            db.session.commit()
            return new_property
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
            'name': self.name,
            'unit_type': self.unit_type.name,
            'unit_price': self.unit_price,
            'unit_period': self.unit_period.name,
            'address': self.address,
            'images': self.images
        }
