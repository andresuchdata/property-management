from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String(required=True, validate=validate.Length(max=50))
    last_name = fields.String(required=True, validate=validate.Length(max=50))
    nik = fields.String(required=True, validate=validate.Length(max=20))
    email = fields.Email(required=True, validate=validate.Length(max=120))
    phone = fields.String(required=True, validate=validate.Length(max=20))
    is_active = fields.Boolean(dump_only=True)
    profile_picture = fields.String(allow_none=True, validate=validate.Length(max=255))

    class Meta:
        ordered = True

class UserWriteSchema(UserSchema):
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=8))

class UserReadSchema(UserSchema):
    pass

class UserReadAllSchema(UserReadSchema):
    # for optimized loading
    property_optimized = fields.Nested('PropertyReadSchema', dump_only=True)
    user_optimized = fields.Nested('UserReadSchema', dump_only=True)

    total_price = fields.Method("get_total_price")

    def get_total_price(self, obj):
        return f"${obj.total_price:.2f}"

    @classmethod
    def serialize_optimized(cls, rentals):
        # Assume rentals are pre-loaded with their related data
        schema = cls(many=True)
        data = schema.dump(rentals)
        for item, rental in zip(data, rentals):
            item['property'] = rental.property
            item['user'] = rental.user
        return data