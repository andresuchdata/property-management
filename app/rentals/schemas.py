from marshmallow import Schema, fields, validate

class RentalSchema(Schema):
    id = fields.String(dump_only=True)
    total_price = fields.Float(required=True, validate=validate.Range(min=0))
    period = fields.Integer(required=True, validate=validate.Range(min=1))
    property_id = fields.Integer(required=True)
    user_id = fields.String(required=True)

    class Meta:
        ordered = True

class RentalWriteSchema(RentalSchema):
    pass

class RentalReadSchema(RentalSchema):
    property = fields.Nested('PropertyReadSchema', dump_only=True)
    user = fields.Nested('UserReadSchema', dump_only=True)
    
    total_price = fields.Method("format_total_price", dump_only=True)

    def format_total_price(self, obj):
        return f"${obj.total_price:.2f}"