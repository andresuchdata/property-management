from marshmallow import Schema, fields, post_dump
from marshmallow_enum import EnumField
from app.properties.models import UnitType, UnitPeriod

class PropertySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    unit_type = EnumField(UnitType, by_value=True, required=True)
    unit_price = fields.Float(required=True)
    unit_period = EnumField(UnitPeriod, by_value=True, required=True)
    address = fields.Str(required=False)
    images = fields.List(fields.Str(), required=False)

    class Meta:
        ordered = True

class PropertyWriteSchema(PropertySchema):
    pass

class PropertyReadSchema(PropertySchema):
    unit_price = fields.Method("format_price", dump_only=True)

    def format_price(self, obj):
        return f"${obj.unit_price:.2f}"