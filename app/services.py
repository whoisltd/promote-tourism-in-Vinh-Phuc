from datetime import time
from re import template
from flask import render_template
from flask.helpers import make_response
from app import app
from sqlalchemy import func
from app.models import *
from flask import json, render_template, request, redirect, jsonify
from flask_paginate import Pagination, get_page_parameter
per_page = 6
@app.route('/services', methods=['GET', 'POST'])
def def_service():
    try:
        page = int(request.args.get(get_page_parameter(), 1))  # phân trang
    except ValueError:
        page = 1
    i=(page-1)*per_page     # lấy dịch vụ từ 1 đến 6 hoặc 6 đến 12
    services = Services.query.all()  # lấy ra toàn bộ
    type_services = Services.query.\
    with_entities(Services.type.label('type'), func.count(Services.type).\
    label('quantity')).group_by(Services.type).all()
    areas = Tourist_area.query.all()
    pagination = Pagination(page=page,per_page=per_page, total=len(services), search=False, record_name='services', href='/services1?page={0}')
    return render_template('services/index.html', type_services=type_services, areas=areas, services=services[i:i+per_page], pagination=pagination)
    
@app.route('/services1', methods=['GET', 'POST'])
def services1():
    print('this is json ', request.get_json())
    try:
        page = int(request.args.get(get_page_parameter(), 1))
        print("this is page", page)
    except ValueError:
        page = 1
    try:
        areas = request.get_json()['areas']
        types = request.get_json()['types']
        print("this is type: ", types)
        i=(page-1)*per_page
        services = Services.query.filter(Services.type.in_(types) & Services.id_tourist_area.in_(areas)).all()
        print("this is ser: ", services)
    except Exception:
        print("have except")
    pagination = Pagination(page=page,per_page=per_page, total=len(services), search=False, record_name='services')
    return render_template('services/items.html', services=services[i:i+per_page], pagination=pagination)

