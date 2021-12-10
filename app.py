from flask import Flask
from flask_migrate import Migrate
import os

import config
from extensions import db
from blueprints import entry_bp, api_bp, user_bp

out_dir = os.path.abspath('.') + os.path.sep + 'dist'
assets_dir = out_dir + os.path.sep + 'assets'

app = Flask(__name__, template_folder=out_dir, static_folder=assets_dir)
app.config.from_object(config)
db.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(entry_bp)
app.register_blueprint(api_bp)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
