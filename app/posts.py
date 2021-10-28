from flask import render_template
from app import app
from app.models import *

@app.route('/posts')
def posts():
    return render_template('posts.html')