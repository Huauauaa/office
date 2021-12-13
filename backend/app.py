import os
from os import error

from flask import Flask, g, session
from flask_migrate import Migrate

import config as config
from blueprints import api_bp, auth_bp, entry_bp, user_bp
from extensions import db, ma
from models.UserModel import UserModel

out_dir = os.path.abspath('.') + os.path.sep + 'dist'
assets_dir = out_dir + os.path.sep + 'assets'

app = Flask(__name__, template_folder=out_dir, static_folder=assets_dir)
app.config.from_object(config)
db.init_app(app)
ma.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(entry_bp)
app.register_blueprint(api_bp)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            g.user = user
        except error:
            g.user = None


@app.context_processor
def context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run(debug=True, port=8888)
