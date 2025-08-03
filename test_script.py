import requests

url = 'http://localhost:4040/send-email'

payload = {
    "email": "stephenalexreid@icloud.com",
    "subject": "Test Subject",
    "message": "This is a test email sent from Flask microservice.",
    "auth_key": "1234567890ABCDE"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
