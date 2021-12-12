from extensions import db
from datetime import datetime


class UserModel(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
