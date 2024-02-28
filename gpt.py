from flask import Flask, jsonify
import pandas as pd
import json
import requests

app = Flask(__name__)

# Define the path to the Excel file
excel_file = r'C:\\Users\\shiva\\Documents\\demo.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

# Define the generate_json_data function
def generate_json_data(df):
    data = {
        "template_name": "welcome_wati_v1",
        "parameters": []
    }

    # Convert data to JSON without escaping double quotes
    for i in df.index:
        name = df["Name"][i]
        a = {"name": name}
        data["parameters"].append(a)

    json_data = data
    return json_data

@app.route('/')
def index():
    # Call the generate_json_data function
    json_data_1 = generate_json_data(df)

    # Send JSON data to the endpoint
    url = "https://app-server.wati.io/api/v1/welcome_wati_v1"
    headers = {
        "content-type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwZjUxMTY3MS00ZGYyLTQzYjktODM3Zi0yOTVjZjZmYzdlMDYiLCJ1bmlxdWVfbmFtZSI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsIm5hbWVpZCI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsImVtYWlsIjoic2hpdmFneWFuZXNod2FyMDZAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDIvMTUvMjAyNCAxMDoxMDoyMiIsImRiX25hbWUiOiJ3YXRpX2FwcF90cmlhbCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlRSSUFMIiwiZXhwIjoxNzA4NjQ2NDAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZwpcTILk5wxfzd7p9tb_GPcTDDte-phMwew19KltpuA"
    }
    response = requests.post(url, json=json_data_1, headers=headers)

    return jsonify(json_data_1)

if __name__ == '__main__':
    app.run(debug=True)