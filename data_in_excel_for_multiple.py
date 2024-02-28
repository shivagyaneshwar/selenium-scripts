from flask import Flask, jsonify
import time 

# Import pandas and json here
import pandas as pd
import json
from wati_function import send_template_message

# Define the path to the Excel file
excel_file = r'C:\\Users\\shiva\\Documents\\demo.xlsx'
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwZjUxMTY3MS00ZGYyLTQzYjktODM3Zi0yOTVjZjZmYzdlMDYiLCJ1bmlxdWVfbmFtZSI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsIm5hbWVpZCI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsImVtYWlsIjoic2hpdmFneWFuZXNod2FyMDZAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDIvMTUvMjAyNCAxMDoxMDoyMiIsImRiX25hbWUiOiJ3YXRpX2FwcF90cmlhbCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlRSSUFMIiwiZXhwIjoxNzA4NjQ2NDAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZwpcTILk5wxfzd7p9tb_GPcTDDte-phMwew19KltpuA"
# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

#reciever_list
reciever=[]
reciever_template={
    "whatsappNumber": "string",
    "customParams":[
         {
          "name": "name",
          "value": "string"
        }
    ]
}

for i in df.index:
    print(df['Name'][i])
    print(df['Phone number'][i])
    reciever_template['whatsappNumber']=str(df['Phone number'][i])
    reciever_template['customParams'][0]['value']=df['Name'][i]
    print(reciever_template)
    reciever.append(reciever_template)
print(reciever)
    
