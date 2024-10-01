from models import Property
from schemas import PropertySchema

class PropertyService:
    @staticmethod
    def get_paginated_properties(page=1, per_page=10):
        paginated_properties = Property.query.paginate(page=page, per_page=per_page, error_out=False)
        
        schema = PropertySchema(many=True)
        return {
            'items': schema.dump(paginated_properties.items),
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': paginated_properties.total,
                'pages': paginated_properties.pages,
                'has_next': paginated_properties.has_next,
                'has_prev': paginated_properties.has_prev,
            }
        }

    @staticmethod
    def get_property(property_id):
        return Property.query.get(property_id)

    @staticmethod
    def create_property(data):
        schema = PropertySchema()
        validated_data = schema.load(data)
        new_property = Property(**validated_data)
        new_property.save()
        return schema.dump(new_property)

    @staticmethod
    def update_property(property_id, data):
        property = Property.query.get(property_id)
        if property:
            schema = PropertySchema(partial=True)
            validated_data = schema.load(data)
            for key, value in validated_data.items():
                setattr(property, key, value)
            property.save()
            return schema.dump(property)
        return None

    @staticmethod
    def delete_property(property_id):
        property = Property.query.get(property_id)
        if property:
            property.delete()
            return True
        return False