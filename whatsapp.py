import requests
from data_in_excel import a

url = "https://app-server.wati.io/api/v1/sendTemplateMessage"

headers = {"content-type": a}

response = requests.post(url, headers=headers)

print(response.text)