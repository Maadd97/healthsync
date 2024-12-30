from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory store (temporary)
appointments = []

# 1. Serve the HTML form when user visits "/"
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")  # Looks for templates/index.html

# 2. Handle form submissions (POST /appointments)
@app.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.json  # Read JSON from POST body
    # You could do extra validation here if needed

    # Generate an appointment ID or something similar
    appointment_id = f"appt_{len(appointments)+1}"

    # Store the appointment in memory
    new_appointment = {
        "appointment_id": appointment_id,
        "doctor": data["doctor"],
        "date": data["date"],
        "time": data["time"],
        "patient_name": data["name"],
        "patient_email": data["email"],
    }
    appointments.append(new_appointment)

    # Return a JSON response
    return jsonify({
        "message": "Appointment created successfully!",
        "appointment_id": appointment_id
    }), 201

# (Optional) GET /appointments to see them all
@app.route("/appointments", methods=["GET"])
def list_appointments():
    return jsonify(appointments), 200

if __name__ == "__main__":
    # For local dev usage
    app.run(host="0.0.0.0", port=5001)
