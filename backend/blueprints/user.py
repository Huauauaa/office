from config import API_PREFIX
from flask import Blueprint, jsonify
from decorators import login_required
from models.UserModel import UserModel
from schemas.UserSchema import UserSchema

bp = Blueprint('user', __name__, url_prefix=API_PREFIX + '/users')


@bp.route('')
@login_required
def all():
    result = UserModel.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(result)), 200


@bp.route('/<int:id>')
def one(id):
    result = UserModel.query.get(id)
    user_schema = UserSchema()
    return user_schema.dump(result), 200
