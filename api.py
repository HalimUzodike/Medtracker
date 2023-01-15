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
    print(med)
    return jsonify(insert_medication(med))


@app.route('/api/meds/', methods=['GET'])
def get_all_meds():
    return jsonify(get_meds())

# """TEST AND FIX THIS API ROUTE."""
# @app.route('/api/meds/<name>', methods=['GET'])
# def get_med_by_name(name):
#     return jsonify(get_med_by_name(name))


@app.route('/api/meds/update/', methods=['PUT'])
def update_med():
    med = request.get_json()
    return jsonify(update_med(med))


# @app.route('/api/meds/delete/', methods=['DELETE'])
# def delete_meds(name):
#     return jsonify(delete_med(name))


@app.route('/api/meds/delete/', methods=['DELETE'])
def delete_meds(name):
    return jsonify(delete_med(name))

