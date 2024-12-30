# microservices/patient-record-service/app.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# In-memory store (replace with a database in production)
patients = {}

@app.route("/patients", methods=["POST"])
def create_patient():
    data = request.json
    patient_id = data.get("patient_id")
    patients[patient_id] = data
    return jsonify({"message": "Patient created", "patient": data}), 201

@app.route("/patients/<patient_id>", methods=["GET"])
def get_patient(patient_id):
    patient = patients.get(patient_id)
    if not patient:
        return jsonify({"message": "Patient not found"}), 404
    return jsonify(patient), 200

@app.route("/patients/<patient_id>", methods=["PUT"])
def update_patient(patient_id):
    if patient_id not in patients:
        return jsonify({"message": "Patient not found"}), 404
    data = request.json
    patients[patient_id].update(data)
    return jsonify({"message": "Patient updated", "patient": patients[patient_id]}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
