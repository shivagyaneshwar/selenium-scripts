from flask import Flask, jsonify
import time 
import smtplib as sm
from email.mime.multipart import MIMEMultipart #for files
from email.mime.text import MIMEText #for text

# Import pandas and json here
import pandas as pd
import json
from wati_function import send_template_message

# Define the path to the Excel file
excel_file = r'C:\\Users\\shiva\\Documents\\demo.xlsx'
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwZjUxMTY3MS00ZGYyLTQzYjktODM3Zi0yOTVjZjZmYzdlMDYiLCJ1bmlxdWVfbmFtZSI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsIm5hbWVpZCI6InNoaXZhZ3lhbmVzaHdhcjA2QGdtYWlsLmNvbSIsImVtYWlsIjoic2hpdmFneWFuZXNod2FyMDZAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDIvMTUvMjAyNCAxMDoxMDoyMiIsImRiX25hbWUiOiJ3YXRpX2FwcF90cmlhbCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlRSSUFMIiwiZXhwIjoxNzA4NjQ2NDAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZwpcTILk5wxfzd7p9tb_GPcTDDte-phMwew19KltpuA"
# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)
list_of_emails=[]
for i in df.index:
    # print(df['Email'])
    list_of_emails.append(df['Email'][i])
print(list_of_emails)
try:
    server=sm.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('shivagyaneshwar06@gmail.com','johncenashiva')
    from_='shivagyaneshwar06@gmail.com'
    to_=list_of_emails
    message=MIMEMultipart("alternative")
    message['Subject']='This is just a testing message'
    message['from']='shivagyaneshwar06@gmail.com'
    html='''
    <html>
    <head>
    </head>
    <body>
        <h1> Learning to test</h1>
        <h2> email automation</h2>
        <p>Test Paragraph</p>
        <button style='padding:20px;background:green">verify</button>
    </html>
    '''
    text=MIMEText(html,'html')
    message.attach()
    server.send=(from_,to_,message.as_string())
    print('message has been sent to mails')
except Exception as e:
    print(e)