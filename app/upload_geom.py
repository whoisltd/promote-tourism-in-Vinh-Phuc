from datetime import time
from re import template
from flask import render_template
from app import app
from sqlalchemy import func
from app.models import *
from flask import json, render_template, request, redirect, jsonify

geojson = '{"crs":{"type": "name", "properties": {"name": "EPSG:4326"}},"type": "Point","coordinates": [21.455735039183423, 105.64349402109205]}'

@app.route('/upload_geom/<int:id>', methods=['GET', 'POST'])
def upload_geom(id):
    """
    Upload geom to database
    with EPSG:4326
    """
    db.session.query(Place).filter(Place.id == id).update({Place.geom: func.ST_GeomFromGeoJSON(geojson)})
    if db.session.commit():
        return 'upload success'
    return 'upload fail'