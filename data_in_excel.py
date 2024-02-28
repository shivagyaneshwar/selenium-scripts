from flask import Flask, jsonify
import time 

# Import pandas and json here
import pandas as pd
import json
from wati_function import send_template_message

# Define the path to the Excel file
excel_file = r'C:\\Users\\shiva\\Documents\\demo.xlsx'
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJlMzE1YjhlNi0yZGJkLTQ0YWQtODkwNS0zYzgyZWY3MmRiZjIiLCJ1bmlxdWVfbmFtZSI6Im5hZ2FyYWp1LmdhamphbGFAY2hpZGhhZ25pLmNvbSIsIm5hbWVpZCI6Im5hZ2FyYWp1LmdhamphbGFAY2hpZGhhZ25pLmNvbSIsImVtYWlsIjoibmFnYXJhanUuZ2FqamFsYUBjaGlkaGFnbmkuY29tIiwiYXV0aF90aW1lIjoiMDIvMjgvMjAyNCAwOToxOTo1NSIsImRiX25hbWUiOiIxMTYxODIiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBRE1JTklTVFJBVE9SIiwiZXhwIjoyNTM0MDIzMDA4MDAsImlzcyI6IkNsYXJlX0FJIiwiYXVkIjoiQ2xhcmVfQUkifQ.ZjBw-bcllfgfNcptl5bLNQD7DtZdKpx--lcT_Ux_eTk"
# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)
for i in df.index:
    print(df['Name'][i])
    print(df['Phone number'][i])
    response = send_template_message(str(df['Phone number'][i]),"welcome_wati_v1", [{'name':'name','value':df['Name'][i]}], token)
    print(response)
