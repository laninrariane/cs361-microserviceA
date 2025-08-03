###################################################
#
# Stephen Reid
# 08/03/2025
# CS361
# Microservice A
#
# Accepts JSON containing email, subject, message, and auth key and sends email
# to address based on data received
#
###################################################

from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# Set credentials for sender email address and set auth key
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""
AUTH_KEY = "1234567890ABCDE"


@app.route("/send-email", methods=["POST"])
def send_email():
    """Receives HTTP POST, sends email message, and returns HTTP status based
    on result (success or failure)"""

    data = request.get_json()

    # Field validation
    req_fields = ["email", "subject", "message", "auth_key"]
    if not all(field in data for field in req_fields):
        return jsonify({"status": "failure", "error": "Missing required fields"}), 400

    # Check auth key (optional)
    # if data['auth_key'] != AUTH_KEY:
    #     return jsonify({"status": "failure", "error": "Auth key invalid or missing"}), 403
    
    # Compose email and send it
    try:
        msg = EmailMessage()
        msg['Subject'] = data['subject']
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = data['email']
        msg.set_content(data['message'])

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

    except Exception as e:
        return jsonify({"status": "failure", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=4040) 