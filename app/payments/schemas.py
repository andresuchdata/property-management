from marshmallow import Schema, fields, validate, post_dump
from .models import Currency

class PaymentSchema(Schema):
    id = fields.String(dump_only=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0))
    currency = fields.Enum(Currency, by_value=True, required=True)
    payment_status = fields.Boolean(required=True)
    rental_id = fields.String(required=True)
    transaction_id = fields.String(allow_none=True)
    payment_method = fields.String(allow_none=True)
    payment_date = fields.DateTime(allow_none=True)

    class Meta:
        ordered = True

class PaymentReadSchema(PaymentSchema):
    # Inheriting from PaymentSchema
    # The PaymentReadSchema will inherit all the fields defined in PaymentSchema.
    # We can then override or add additional fields and behavior specific to the read schema.

    @post_dump
    def format_amount(self, data, **kwargs):
        amount = float(data['amount'])
        currency = data['currency']
        if currency == 'usd':
            data['amount'] = f"${amount:,.2f}"
        elif currency == 'idr':
            data['amount'] = f"Rp {amount:,.0f}"
        return data