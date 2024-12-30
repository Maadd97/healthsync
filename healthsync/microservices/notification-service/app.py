# microservices/notification-service/app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def send_notification():
    data = request.json
    # Simulate sending an email or SMS
    # e.g., using Twilio or SMTP
    print(f"Sending notification to {data['recipient']}: {data['message']}")
    return jsonify({"message": "Notification sent"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
