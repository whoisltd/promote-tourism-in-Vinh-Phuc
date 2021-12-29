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
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    try:
        page = int(request.args.get(get_page_parameter(), 1))
    except ValueError:
        page = 1
    i=(page-1)*per_page
    posts = Posts.query.all()
    areas = Tourist_area.query.all()
    pagination = Pagination(page=page,per_page=per_page, total=len(posts), search=False, record_name='posts', href='/posts1?page={0}')
    return render_template('posts/index.html', areas=areas, posts=posts[i:i+per_page], pagination=pagination)
    
@app.route('/posts1', methods=['GET', 'POST'])
def posts1():
    try:
        page = int(request.args.get(get_page_parameter(), 1))
    except ValueError:
        page = 1
    areas = request.get_json()['areas']
    i=(page-1)*per_page
    posts = Posts.query.filter(Posts.id_tourist_area.in_(areas)).all()  
    pagination = Pagination(page=page,per_page=per_page, total=len(posts), search=False, record_name='posts')
    return render_template('posts/items.html', posts=posts[i:i+per_page], pagination=pagination)

@app.route('/posts/<int:id>', methods=['GET', 'POST'])
def postDetail(id):
    postIds = Posts.query.filter(Posts.id==id)
    return render_template('posts/postDetail.html', postIds=postIds)