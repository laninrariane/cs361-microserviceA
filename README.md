# 📧 Microservice A - Email Sender
**Stephen Reid**  
**CS361** 
**08/03/2025**

---

## 📜 Communication Contract

This microservice listens on port `4040` and accepts HTTP POST requests at the `/send-email` route. It expects a JSON payload with required fields and responds with a status indicating success or failure.

Once defined, this communication contract will not change.

---

## ✅ Requesting Data

To request the service, send an HTTP POST request to:
http://localhost:4040/send-email

### Required JSON Fields:
| Field     | Type   | Description                  |
|-----------|--------|------------------------------|
| `email`   | string | Destination email address    |
| `subject` | string | Email subject line           |
| `message` | string | Body of the email            |
| `auth_key`| string | Shared secret key            |

### 🔧 Example Request (Python):
```python
import requests

url = 'http://localhost:4040/send-email'

payload = {
    "email": "test_email@email.com,
    "subject": "Test Email",
    "message": "Here is your test message...",
    "auth_key": "1234567890ABCDE"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
```

## 📩 Receiving Data

Client will receive a JSON response with following format:

On Success:
```json
{
  "status": "success",
  "message": "Email sent successfully"
}
```

On Failure:
```json
{
  "status": "failure",
  "error": "Detailed error message"
}
```

Standard HTTP status codes are used to handle different outcomes:


| Code      | Message               | Description                  |
|-----------|-----------------------|------------------------------|
| 200       | OK                    | Email sent successfully      |
| 400       | Bad Request           | Field(s) missing             |
| 403       | Forbidden             | Invalid or missing auth key  |
| 500       | Internal Server Error | Email failed to send         |

## 📊 UML Diagram
<img width="590" height="334" alt="Untitled" src="https://github.com/user-attachments/assets/080cef31-ee10-4e47-aefa-3efbcb8192f0" />

