import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cannot-to-guess'
    JSON_AS_ASCII = True
    # postgres://user:password@localhost:5432/dbname
    