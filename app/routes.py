from flask import render_template
import csv 
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

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
da = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/import-data")
def importData():
    f = open("posts.csv")
    postsDataFile = csv.reader(f)
    for title, content, image, id_tourist_area, id_place, id_review in postsDataFile:
        post = Posts(title=title, content=content, image=image, id_tourist_area=id_tourist_area, id_place=id_place, id_review=id_review )
        db.session.add(post)
    db.session.commit()
    return "oke"

if __name__ == "__main__":
    with app.app_context():
        importData()