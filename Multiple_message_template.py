import requests
import json

def send_template_message(template_name, parameters,brodcast_name, token):
    # Define the URL with the recipient's WhatsApp number as a query parameter
    url = f"https://app-server.wati.io/api/v1/sendTemplateMessages"

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"  # Replace with your actual token
    }

    # Define the payload
    payload = {
        "template_name": template_name,
        "broadcast_name": brodcast_name,
        "receivers": parameters
    }

    # Convert payload to JSON
    json_payload = json.dumps(payload)

    # Send POST request
    response = requests.post(url, headers=headers, data=json_payload)
    try:
        print(1)
        return response.json()
    except:
        print(2)
        return response

# Example
template_name = "welcome_wati_v1"
parameters = [{'whatsappNumber': '8247212035', 'customParams': [{'name': 'name', 'value': 'sanjay'}]}, {'whatsappNumber': '8247212035', 'customParams': [{'name': 'name', 'value': 'sanjay'}]}, {'whatsappNumber': '8247212035', 'customParams': [{'name': 'name', 'value': 'sanjay'}]}]
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwZjUxMTY3MS00ZGYyLTQzYjktODM3Zi0yOTVjZjZmYzdlMDYiLCJ1bmlxdWVfbmFtZSI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsIm5hbWVpZCI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsImVtYWlsIjoic2hpdmFneWFuZXNod2FyMDZAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDIvMTUvMjAyNCAxMDoxMDoyMiIsImRiX25hbWUiOiJ3YXRpX2FwcF90cmlhbCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlRSSUFMIiwiZXhwIjoxNzA4NjQ2NDAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZwpcTILk5wxfzd7p9tb_GPcTDDte-phMwew19KltpuA"
brodcast_name="None"
response = send_template_message(template_name, parameters,brodcast_name, token)
print(response)