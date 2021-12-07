from flask import Flask, render_template, jsonify
import os, config
from flask_migrate import Migrate
from extensions import db
from models.UserModel import UserModel

out_dir = os.path.abspath('.') + os.path.sep + 'dist'
assets_dir = out_dir + os.path.sep + 'assets'

app = Flask(__name__, template_folder=out_dir, static_folder=assets_dir)
app.config.from_object(config)
db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/users')
def users():
    users = UserModel.query.all()
    print(users)
    return jsonify(users)
