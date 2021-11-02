from datetime import time
from flask import render_template
from flask.helpers import make_response
from app import app
from sqlalchemy import func
from app.models import *
from flask import json, render_template, request, redirect, jsonify
from flask_paginate import Pagination, get_page_parameter

per_page = 6
@app.route('/services', methods=['GET', 'POST'])
def def_service(page_num=1):
    services = Services.query.paginate(page=page_num, per_page=per_page, error_out=False)
    type_services = Services.query.\
    with_entities(Services.type.label('type'), func.count(Services.type).\
    label('quantity')).group_by(Services.type).all()
    areas = Tourist_area.query.all()
    return render_template('services/index.html', services=services, type_services=type_services, areas=areas)

@app.route('/services/<int:page_num>', methods=['GET', 'POST'])
def services(page_num):
    services = Services.query.paginate(page=page_num, per_page=per_page, error_out=False)
    return render_template('services/items.html', services=services)

@app.route('/load_page/<int:page_num>', methods=['GET', 'POST'])
def load_page(page_num):
    services = Services.query.paginate(page=page_num, per_page=per_page, error_out=False)
    return render_template('services/load_page.html', services=services)
