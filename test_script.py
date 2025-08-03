import requests

url = 'http://localhost:4040/send-email'

payload = {
    "email": "stephenalexanderreid@gmail.com",
    "subject": "Test Recipe Email",
    "message": "Here is your test recipe:...",
    "auth_key": "1234567890ABCDE"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
