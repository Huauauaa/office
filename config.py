import os


HOSTNAME = os.environ.get('DB_HOSTNAME') or 'localhost'
PORT = os.environ.get('DB_PORT') or '3306'
DATABASE = os.environ.get('DB_DATABASE') or 'office'
USERNAME = os.environ.get('DB_USERNAME')
PASSWORD = os.environ.get('DB_PASSWORD')
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'asdasdfasdfasdfasdfasd'
