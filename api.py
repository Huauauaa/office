from flask import Flask, render_template, jsonify

import os

out_dir = os.path.abspath('.') + os.path.sep + 'dist'
assets_dir = out_dir + os.path.sep + 'assets'

app = Flask(__name__, template_folder=out_dir, static_folder=assets_dir)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/api/users')
def users():
    users = [{'id': 1, 'name': 'user1'}, {'id': 2, 'name': 'user2'}]
    return jsonify(users)
