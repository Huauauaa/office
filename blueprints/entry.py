from flask import Blueprint, render_template

bp = Blueprint('entry', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')
