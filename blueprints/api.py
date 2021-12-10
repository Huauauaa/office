from flask import Blueprint
import app

bp = Blueprint('api', __name__, url_prefix=app.config.API_PREFIX)


@bp.route('')
def index():
    return {'data': 'api'}
