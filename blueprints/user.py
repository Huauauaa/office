from flask import Blueprint, jsonify
from models.UserModel import UserModel

bp = Blueprint('user', __name__, url_prefix='/api/users')


@bp.route('')
def all():
    result = UserModel.query.all()
    return jsonify(list(map(lambda item: item.schema(), result))), 200


@bp.route('/<int:id>')
def one(id):
    result = UserModel.query.get(id)
    return result.schema()
