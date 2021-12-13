from config import API_PREFIX
from extensions import db
from flask import Blueprint, flash, redirect, request, session, url_for
from models.UserModel import UserModel
from schemas.LoginSchema import LoginSchema
from schemas.RegisterSchema import RegisterSchema
from schemas.UserSchema import UserSchema
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix=f'{API_PREFIX}/auth')


@bp.route('/login', methods=['POST'])
def login():
    login_schema = LoginSchema()
    user_schema = UserSchema()
    errors = login_schema.validate(request.json)
    if errors:
        return errors, 400
    username = request.json.get('username')
    password = request.json.get('password')
    try:
        user = UserModel.query.filter_by(username=username).first_or_404()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return user_schema.dump(user)
        else:
            return '邮箱和密码不匹配！', 400
    except:
        return '邮箱和密码不匹配！', 404


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.login'))


@bp.route('/register', methods=['POST'])
def register():
    register_schema = RegisterSchema()
    errors = register_schema.validate(request.json)
    if errors:
        return errors, 400

    username = request.json.get('username')
    password = request.json.get('password')

    hash_password = generate_password_hash(password)
    user = UserModel(username=username, password=hash_password)
    db.session.add(user)
    db.session.commit()
    return 'Registered', 201
