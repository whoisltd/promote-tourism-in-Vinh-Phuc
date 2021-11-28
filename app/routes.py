from flask import render_template
from app import app
from app.models import *
from flask import json, render_template, request, redirect
from flask.json import jsonify
from sqlalchemy import func

# from app.forms import editBuildingForm, editTreeForm
from flask.helpers import url_for
from flask_wtf import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# from config import Config

engine = create_engine(
    "postgresql://jxjsmnnorqvphr:d72266739d8fa38e2d4d814a9ea062d558710148b55a8a0cd037cf5fb57a04e4@ec2-18-210-95-55.compute-1.amazonaws.com:5432/d8gc0s3lfimj2g"
)
da = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

