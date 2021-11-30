from datetime import time
from re import template
from flask import render_template
from app import app
from sqlalchemy import func
from app.models import *
from flask import json, render_template, request, redirect, jsonify

geojson = '{"crs":{"type": "name", "properties": {"name": "EPSG:4326"}},"type": "Point","coordinates": [105.64662413815077, 21.455960226790893]}'

@app.route('/upload_geom/<int:id>', methods=['GET', 'POST'])
def upload_geom(id):
    """
    Upload geom to database
    with EPSG:4326
    """
    db.session.query(Tourist_area).filter(Tourist_area.id == id).update({Tourist_area.geom: func.ST_GeomFromGeoJSON(geojson)})
    db.session.commit()
    return 'oke'