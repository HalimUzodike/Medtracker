from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Medicaiton.db"
db = SQLAlchemy(app)



class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    medication = db.Column(db.String(250), nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(250))

db.create_all()


def add_medication_record(name, medication, frequency, notes = ''):
    new_medication = Medication(name, medication, frequency, notes)
    db.session.add(new_medication)


def read_all_records():
    all_medication = db.session.query(Medication).all()
    return all_medication


def query_medication(medication_name):
    medicine = Medication.query.filter_by(medication=medication_name)
    return medicine


def update_record_medication(medication_name, new_medication):
    query_to_update = Medication.query.filter_by(medication=medication_name)
    query_to_update.medication = new_medication


def delete_record(medication):
    med_to_delete = Medication.query.get(medication)
    db.session.delete(med_to_delete)



add_medication_record("Odin", "Tylenol", 4, "take with water ")






