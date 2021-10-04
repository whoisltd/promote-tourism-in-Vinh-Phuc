import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cannot-to-guess'
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # postgres://user:password@localhost:5432/dbname
    # clever-cloud
    SQLALCHEMY_DATABASE_URI = 'postgres://bngy8ookxwsmy49rkk7c:ANQDOHmglqkfuvw5CP8U@bngy8ookxwsmy49rkk7c-postgresql.services.clever-cloud.com:5432/bngy8ookxwsmy49rkk7c'
