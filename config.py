import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cannot-to-guess'
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # postgres://user:password@localhost:5432/dbname

    SQLALCHEMY_DATABASE_URI = 'postgresql://jxjsmnnorqvphr:d72266739d8fa38e2d4d814a9ea062d558710148b55a8a0cd037cf5fb57a04e4@ec2-18-210-95-55.compute-1.amazonaws.com:5432/d8gc0s3lfimj2g'    

