from datetime import time
from re import template
from flask import render_template
from flask.helpers import make_response
from app import app
from sqlalchemy import func
from app.models import *
from flask import json, render_template, request, redirect, jsonify

@app.route("/api/v1/areas")
def areas_api():
    """
    API for areas
    Return an GeoJSON object with all the areas
    API will have structure like below:
    {
        "features": [
            {
                "geometry": {
                    "coordinates": [
                        21.4557350391834, 
                        105.643494021092
                    ], 
                "type": "Point"
            },  
                "properties": {
                    "description": "Khu du lịch Tam Đảo, Tỉnh Vĩnh Phúc", 
                    "id": 1, 
                    "image": "{\"images/services/restaurant.jpg\",\"images/services/restaurant1.jpg\"}", 
                    "title": "Tam đảo",
                }, 
                "type": "Feature"
            }, 
        ]
    }
    """
    areas = db.session.query(Tourist_area.id,Tourist_area.name, 
                            Tourist_area.description,Tourist_area.image,
                            func.ST_AsGeoJSON(func.ST_Transform(Tourist_area.geom, 4326)).label('geometry')).all()
    areas_feature = []
    for area in areas:
        properties_temp = {
            "id": area.id,
            "name": area.name,
            "description": area.description,
            "image": area.image,
        }
        if area.geometry is not None:
            geometry_temp = json.loads(area.geometry)
        else:
            geometry_temp = ""
        feature = {
            "type": "Feature",
            "properties": properties_temp,
            "geometry": geometry_temp
        }
        areas_feature.append(feature)

    return jsonify({
        "features": areas_feature
    })

@app.route("/api/v1/places")
def places_api():
    """
    API for places
    Return an GeoJSON object with all the places
    API will have structure like below:
    {
        "features": [
            {
                "geometry": {
                    "coordinates": [
                        21.4557350391834, 
                        105.643494021092
                    ], 
                "type": "Point"
            }, 
                "properties": {
                    "description": "Quảng trường trung tâm Tam Đảo là địa điểm vui chơi chính và nằm ngay tại trung tâm của khu 1, thị trấn Tam Đảo. ", 
                    "id": 10, 
                    "id_post": null, 
                    "id_tourist_area": 1, 
                    "image": "{\"images/services/restaurant.jpg\",\"images/services/restaurant1.jpg\"}", 
                    "title": "Quảng Trường Trung Tâm",
                }, 
                "type": "Feature"
            }, 
        ]
    }
    """
    places = db.session.query(Place.id, Place.title, Place.description,
                              Place.image, Place.id_tourist_area, Place.id_post,
                              func.ST_AsGeoJSON(func.ST_Transform(Place.geom, 4326)).label('geometry')).all()
    places_feature = []
    for place in places:
        properties_temp = {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "image": place.image,
            "id_tourist_area": place.id_tourist_area,
            "id_post": place.id_post,
        }
        if place.geometry is not None:
            geometry_temp = json.loads(place.geometry)
        else:
            geometry_temp = ""
        feature = {
            "type": "Feature",
            "properties": properties_temp,
            "geometry": geometry_temp
        }
        places_feature.append(feature)

    return jsonify({
        "features": places_feature
    })

@app.route("/api/v1/services")
def services_api():
    """
    API for services
    Return an GeoJSON object with all the services
    API will have structure like below:
    {
        "features": [{
                "geometry": {
                    "coordinates": [
                        21.4557350391834, 
                        105.643494021092
                    ], 
                "type": "Point"
            }, 
                "properties": {
                    "description": "Nhà hàng đầu tiên tại Tam Đảo", 
                    "id": 10, 
                    "id_tourist_area": 1, 
                    "phone": "0989898989",
                    "email": "nhahang@gmail.com",
                    "image": "{\"images/services/restaurant.jpg\",\"images/services/restaurant1.jpg\"}", 
                    "name": "Nhà hàng Tam Đảo",
                    "type": "restaurant",
                }, 
                "type": "Feature"
            }, 
        ]
    }
    """
    services = db.session.query(Services.id, Services.name, Services.description,
                              Services.image, Services.phone, Services.email, 
                              Services.address, Services.id_tourist_area, Services.type,
                              func.ST_AsGeoJSON(func.ST_Transform(Services.geom, 4326)).label('geometry')).all()
    services_feature = []
    for service in services:
        properties_temp = {
            "id": service.id,
            "name": service.name,
            "description": service.description,
            "image": service.image,
            "phone": service.phone,
            "email": service.email,
            "address": service.address,
            "type": service.type,
            "id_tourist_area": service.id_tourist_area,
        }
        if service.geometry is not None:
            geometry_temp = json.loads(service.geometry)
        else:
            geometry_temp = ""
        feature = {
            "type": "Feature",
            "properties": properties_temp,
            "geometry": geometry_temp
        }
        services_feature.append(feature)

    return jsonify({
        "features": services_feature
    })

@app.route("/api/v1/services/<int:id>")
def service_api(id):
    service = db.session.query(Services.id, Services.name, Services.description,
                              Services.image, Services.phone, Services.email, 
                              Services.address, Services.id_tourist_area, Services.type,
                              func.ST_AsGeoJSON(func.ST_Transform(Services.geom, 4326)).label('geometry')).filter_by(id = id).first()
    services_feature = []
    properties_temp = {
        "id": service.id,
        "name": service.name,
        "description": service.description,
        "image": service.image,
        "phone": service.phone,
        "email": service.email,
        "address": service.address,
        "type": service.type,
        "id_tourist_area": service.id_tourist_area,
    }
    if service.geometry is not None:
        geometry_temp = json.loads(service.geometry)
    else:
        geometry_temp = ""
    feature = {
        "type": "Feature",
        "properties": properties_temp,
        "geometry": geometry_temp
    }
    services_feature.append(feature)

    return jsonify({
        "features": services_feature
    })