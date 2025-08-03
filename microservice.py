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
# To set without hardcoding use following in terminal:
#   export EMAIL_USER=""
#   export EMAIL_PASS=""
EMAIL_ADDRESS = os.getenv("EMAIL_USER", "email@email.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS", "password")
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
    if data["auth_key"] != AUTH_KEY:
        return (
            jsonify({"status": "failure", "error": "Auth key invalid or missing"}),
            403,
        )

    # Compose email and send it
    try:
        msg = EmailMessage()
        msg["Subject"] = data["subject"]
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = data["email"]
        msg.set_content(data["message"])

        print("Sending email...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"status": "success", "message": "Email sent successfully"}), 200

    except Exception as e:
        return jsonify({"status": "failure", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=4040)
