"""Route subdomain to html."""

from flask import render_template
from app import app
#from models import Medication


@app.route('/')
def homepage():
    return render_template('index.html')