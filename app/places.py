from flask import render_template
from app import app
from app.models import *

@app.route("/places")
def places():
    places = Place.query.filter_by(id_tourist_area = 1).all()
    return render_template("places/places.html",places = places)

@app.route("/daiLai")
def daiLai():
    daiLai = Place.query.filter_by(id_tourist_area = 4).all()
    return render_template("places/daiLai.html",daiLai = daiLai)
@app.route("/damVac")
def damVac():
    damVac = Place.query.filter_by(id_tourist_area = 2).all()
    return render_template("places/damVac.html",damVac = damVac)
@app.route("/tayThien")
def tayThien():
    tayThien = Place.query.filter_by(id_tourist_area = 3).all()
    return render_template("places/tayThien.html",tayThien = tayThien)
