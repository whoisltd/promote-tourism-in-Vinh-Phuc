from datetime import time
from re import template
from flask import render_template
from app import app
from sqlalchemy import func
from app.models import *
from flask import json, render_template, request, redirect, jsonify

geojson = ['/images/places/place-1.jpg', '/images/places/place-2.jpg', '/images/places/place-3.jpg', '/images/places/place-4.jpg']
@app.route('/upload_geom', methods=['GET', 'POST'])
def upload_geom():
    """
    Upload geom to database
    with EPSG:4326
    """
    for i in range(len(geojson)):
        db.session.query(Place).filter(Place.id == i+1).update({Place.image: geojson[i]})
    db.session.commit()
    return 'oke'