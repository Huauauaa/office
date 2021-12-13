from config import API_PREFIX
from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix=API_PREFIX)


@bp.route('')
def index():
    return {'data': 'api'}
