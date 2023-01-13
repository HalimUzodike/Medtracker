"""
Single entry-point to resolve import dependencies.
Run this to run the app.
"""

from app import app, create_table

from api import api
from models import *
from views import *

api.init_app(app)


if __name__ == '__main__':
    create_table()
    app.run()