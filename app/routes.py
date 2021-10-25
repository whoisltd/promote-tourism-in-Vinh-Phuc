from flask import render_template
from app import app
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

engine = create_engine('')
da = scoped_session(sessionmaker(bind=engine))


@app.route('/services')
def services():
    return render_template('services.html')
  
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/places")
def places():
    return render_template("places.html")
