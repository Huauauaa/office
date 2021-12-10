from extensions import ma
from models.UserModel import UserModel


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    id = ma.auto_field()
    username = ma.auto_field()
