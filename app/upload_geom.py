from datetime import time
from re import template
from flask import render_template
from app import app
from sqlalchemy import func
from app.models import *
from flask import json, render_template, request, redirect, jsonify

geojson = ['{"crs":{"type": "name", "properties": {"name": "EPSG:4326"}},"type": "Point","coordinates": [105.64472004618987, 21.456268879998778]}',
'{"crs":{"type": "name", "properties": {"name": "EPSG:4326"}},"type": "Point","coordinates": [105.5855035151476, 21.466358627392434]}',
'{"crs":{"type": "name", "properties": {"name": "EPSG:4326"}},"type": "Point","coordinates": [105.59646717616441, 21.30037309018502]}',
'{"crs":{"type": "name", "properties": {"name": "EPSG:4326"}},"type": "Point","coordinates": [105.71497395057379, 21.320349114412867]}']

@app.route('/upload_geom', methods=['GET', 'POST'])
def upload_geom():
    """
    Upload geom to database
    with EPSG:4326
    """
    for i in range(len(geojson)):
        db.session.query(Place).filter(Place.id == i+1).update({Place.geom: func.ST_GeomFromGeoJSON(geojson[i])})
    db.session.commit()
    return 'oke'