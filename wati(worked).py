import requests
import json

# Define the URL
url = "https://app-server.wati.io/api/v1/sendTemplateMessage?whatsappNumber=%2B919000981111"

# Define the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwZjUxMTY3MS00ZGYyLTQzYjktODM3Zi0yOTVjZjZmYzdlMDYiLCJ1bmlxdWVfbmFtZSI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsIm5hbWVpZCI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsImVtYWlsIjoic2hpdmFneWFuZXNod2FyMDZAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDIvMTUvMjAyNCAxMDoxMDoyMiIsImRiX25hbWUiOiJ3YXRpX2FwcF90cmlhbCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlRSSUFMIiwiZXhwIjoxNzA4NjQ2NDAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZwpcTILk5wxfzd7p9tb_GPcTDDte-phMwew19KltpuA"  # Replace with your actual token
}

# Define the payload
payload = {
    "template_name": "welcome_wati_v1",
    "broadcast_name": "None",  # Set to empty if not required
    "parameters": [
        {
            "name": "name",
            "value": "John Doe"
        }
    ]
}

# Convert payload to JSON
json_payload = json.dumps(payload)

# Send POST request
response = requests.post(url, headers=headers, data=json_payload)

# Check the response
print(response.text)