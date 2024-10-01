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