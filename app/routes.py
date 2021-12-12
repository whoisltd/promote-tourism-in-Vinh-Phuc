from flask import render_template
from werkzeug.utils import ArgumentValidationError
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
import os
# from config import Config

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
da = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/createNewItem", methods=["POST"])
def createNewItem():
    print(request.get_json())
    data = request.get_json()
    data["geometry"]["crs"] = {
        "type": "name", "properties": {"name": "EPSG:4326"}}

    print(data["geometry"])

    result = json.dumps(data["geometry"])
    print(result)

    if data["typeMarker"] == "Service":
        service = Services(geom=func.ST_GeomFromGeoJSON(result))
        db.session.add(service)
    elif data["typeMarker"] == "Area":
        area = Tourist_area(geom=func.ST_GeomFromGeoJSON(result))
        db.session.add(area)
    elif data["typeMarker"] == "Place":
        place = Place(geom=func.ST_GeomFromGeoJSON(result))
        db.session.add(place)
    db.session.commit()
    return redirect(url_for('index'))