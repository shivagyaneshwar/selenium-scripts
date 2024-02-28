import requests
import json

def send_template_message(whatsapp_number, template_name, parameters, token):
    # Define the URL with the recipient's WhatsApp number as a query parameter
    url = f"https://app-server.wati.io/api/v1/sendTemplateMessage?whatsappNumber=%2B+91{whatsapp_number}"

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"  # Replace with your actual token
    }

    # Define the payload
    payload = {
        "template_name": template_name,
        "broadcast_name": "Untitled_160220241138",
        "parameters": parameters
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

# Example usage:
whatsapp_number = "+919000981111"
template_name = "welcome_wati_v1"
parameters = [{"name": "name", "value": "John Doe"}]
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwZjUxMTY3MS00ZGYyLTQzYjktODM3Zi0yOTVjZjZmYzdlMDYiLCJ1bmlxdWVfbmFtZSI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsIm5hbWVpZCI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsImVtYWlsIjoic2hpdmFneWFuZXNod2FyMDZAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDIvMTUvMjAyNCAxMDoxMDoyMiIsImRiX25hbWUiOiJ3YXRpX2FwcF90cmlhbCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlRSSUFMIiwiZXhwIjoxNzA4NjQ2NDAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZwpcTILk5wxfzd7p9tb_GPcTDDte-phMwew19KltpuA"

response = send_template_message(whatsapp_number, template_name, parameters, token)
print(response.text)