"""RESTful API"""

from flask import request, jsonify
from flask_restful import Api
from flask_cors import CORS

from app import app, get_meds, delete_med, insert_medication
CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

@app.route('/api/meds/add/', methods=['POST'])
def add_new_med():
    med = request.get_json()
    return jsonify(insert_medication(med))

@app.route('/api/meds/', methods=['GET'])
def get_all_meds():
        return jsonify(get_meds())

@app.route('/api/meds/delete/', methods=['DELETE'])
def delete_meds(name):
    return jsonify(delete_med(name))


#api.add_resource(Meds, '/meds/')
#api.add_resource(UpdateMeds, '/meds/update/')
