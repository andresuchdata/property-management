from .models import Rental
from .schemas import RentalSchema

class RentalService:
    @staticmethod
    def create_rental(data):
        schema = RentalSchema()
        validated_data = schema.load(data)
        new_rental = Rental(**validated_data)
        new_rental.save()
        return schema.dump(new_rental)

    @staticmethod
    def get_rental(rental_id):
        return Rental.query.get(rental_id)

    @staticmethod
    def update_rental(rental_id, data):
        rental = Rental.query.get(rental_id)
        if rental:
            schema = RentalSchema(partial=True)
            validated_data = schema.load(data)
            for key, value in validated_data.items():
                setattr(rental, key, value)
            rental.save()
            return schema.dump(rental)
        return None

    @staticmethod
    def delete_rental(rental_id):
        rental = Rental.query.get(rental_id)
        if rental:
            rental.delete()
            return True
        return False
