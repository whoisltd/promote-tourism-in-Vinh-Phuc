from datetime import time
from re import template
from flask import render_template
from flask.helpers import make_response
from app import app
from sqlalchemy import func
from app.models import *
from flask import json, render_template, request, redirect, jsonify
from flask_paginate import Pagination, get_page_parameter
per_page = 3
@app.route('/services', methods=['GET', 'POST'])
def def_service():
    template = 'services/index.html'
    try:
        page = int(request.args.get(get_page_parameter(), 1))
    except ValueError:
        page = 1
    i=(page-1)*per_page
    services = Services.query.all()
    type_services = Services.query.\
    with_entities(Services.type.label('type'), func.count(Services.type).\
    label('quantity')).group_by(Services.type).all()
    areas = Tourist_area.query.all()
    pagination = Pagination(page=page,per_page=per_page, total=len(services), search=False, record_name='services', href='/services1?page={0}')
    return render_template(template, type_services=type_services, areas=areas, services=services[i:i+per_page], pagination=pagination)
    
@app.route('/services1', methods=['GET', 'POST'])
def services1():
    template = 'services/items.html'
    type1 = None
    print('this is json ', request.get_json())
    try:
        page = int(request.args.get(get_page_parameter(), 1))
        print("this is page", page)
    except ValueError:
        page = 1
    try:
        type1 = request.get_json()['arr']
        print("this is type: ", type1)
        i=(page-1)*per_page
        services = Services.query.filter(Services.type.in_(type1)).all()
        print("this is ser: ", services)
    except Exception:
        print("have except")
    pagination = Pagination(page=page,per_page=per_page, total=len(services), search=False, record_name='services')
    return render_template(template, services=services[i:i+per_page], pagination=pagination)

@app.route('/checks', methods=['GET'])
def checks():
    offset = int(request.args.get('offset'))
    print(offset)
    print(request.args.get('curr'))
    limit = 3
    numbers = Services.query.count()
    services = Services.query.order_by(Services.id.asc()).limit(limit).offset(offset).all()
    output = []
    for service in services:
        output.append({'id': service.id, 'name': service.name})
    next_url = '/checks?limit=' + str(limit) + '&offset=' + str(offset + limit)
    prev_url = '/checks?limit=' + str(limit) + '&offset=' + str(offset - limit)
    curr = '/checks?limit=' + str(limit) + '&offset=' + str(offset - limit) + '&arr=' + str('a')
    return jsonify({'result': output, 'next_url': next_url, 'prev_url': prev_url, 'curr': curr})


# @app.route('/services/filter', methods=['GET', 'POST'])
# @app.route('/services/<int:page_num>', methods=['GET', 'POST'])
# def services(page_num=1):
#     type1 = None
#     type1 = request.get_json()['arr']
#     print(type1)
#     services = Services.query.filter_by(type = 'Khách sạn').all()
#     # print(services)
#     for i in services:
#         print(i)
#     return render_template('services/items.html', services=services)

# @app.route('/services/filter', methods=['GET', 'POST'])
# @app.route('/load_page/<int:page_num>', methods=['GET', 'POST'])
# def load_page(page_num=1):
#     type1 = None
#     try:
#         type1 = request.get_json()['arr']
#         ser = Services.query.filter(Services.type.in_(type1)).all()
#         services = Services.query.ser.paginate(page=page_num, per_page=per_page, error_out=False)
#     except Exception:
#         services = Services.query.paginate(page=page_num, per_page=per_page, error_out=False)
#     return render_template('services/load_page.html', services=services)

# @app.route('/services/filter', methods=['GET', 'POST'])
# def filter():
#     type1 = None
#     type1 = request.get_json()['arr']
#     print(type(type1))
#     print("hello", type1)
#     services = Services.query.filter(Services.type.in_(type1)).all()
#     for i in services:
#         print(i)
#     return render_template('services/items.html', services=services)