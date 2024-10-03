from .. import db
from .models import User
from .schemas import UserSchema

class UserService:
    @staticmethod
    def create_user(data):
        schema = UserSchema()
        validated_data = schema.load(data)
        new_user = User(**validated_data)
        new_user.set_password(data['password'])
        new_user.save()
        return schema.dump(new_user)

    @staticmethod
    def get_user(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if user:
            schema = UserSchema(partial=True)
            validated_data = schema.load(data)
            for key, value in validated_data.items():
                setattr(user, key, value)
            user.save()
            return schema.dump(user)
        return None

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            user.delete()
            return True
        return False

    @staticmethod
    def get_paginated_users(page=1, per_page=10):
        paginated_users = User.query.paginate(page=page, per_page=per_page, error_out=False)
        
        schema = UserSchema(many=True)
        return {
            'items': schema.dump(paginated_users.items),
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': paginated_users.total,
                'pages': paginated_users.pages,
                'has_next': paginated_users.has_next,
                'has_prev': paginated_users.has_prev,
            }
        }