"""RESTful API"""

from flask_restful import Resource, Api

from app import app
from models import Medication



api = Api(app)

med1 = {"name": "Tylenol", "notes": "Take with food", "frequency": 1}
med2 = {"name": "Advil", "notes": "Take with food", "frequency": 1}
meds = {"medications": [med1, med2]}

def api_test(name, notes, frequency):
    medication = {name, notes, frequency}
    return medication

class Meds(Resource):
    def get(self):
        return meds

api.add_resource(Meds, '/meds/')
