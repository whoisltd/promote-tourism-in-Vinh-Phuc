from flask import render_template
from app import app
from app.models import *

@app.route("/places")
def places():
    return render_template("places.html")