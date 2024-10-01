from .models import Payment
from .schemas import PaymentSchema

class PaymentService:
    @staticmethod
    def create_payment(data):
        schema = PaymentSchema()
        validated_data = schema.load(data)
        new_payment = Payment(**validated_data)
        new_payment.save()
        return schema.dump(new_payment)

    @staticmethod
    def get_payment(payment_id):
        return Payment.query.get(payment_id)

    @staticmethod
    def update_payment(payment_id, data):
        payment = Payment.query.get(payment_id)
        if payment:
            schema = PaymentSchema(partial=True)
            validated_data = schema.load(data)
            for key, value in validated_data.items():
                setattr(payment, key, value)
            payment.save()
            return schema.dump(payment)
        return None

    @staticmethod
    def delete_payment(payment_id):
        payment = Payment.query.get(payment_id)
        if payment:
            payment.delete()
            return True
        return False
