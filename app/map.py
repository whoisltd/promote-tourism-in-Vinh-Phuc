from flask import render_template
from app import app
from app.models import *

@app.route("/map")
def map():
    return render_template("map/index.html")