import requests
import json

def send_email(api_key, subject, text_content, html_content, from_email, from_name, to_emails):
    url = f"https://us21.api.mailchimp.com/3.0/messages/send"  # Replace <dc> with your Mailchimp data center prefix (e.g., us21)
    payload = {
        "key": api_key,
        "message": {
            "subject": subject,
            "text": text_content,
            "html": html_content,
            "from_email": from_email,
            "from_name": from_name,
            "to": [{"email": email} for email in to_emails]
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print("Failed to send email. Status code:", response.status_code)
        print("Error message:", response.text)

# Example usage:
api_key = "f94d942c3630d61648cf22306b2a8734-us21"
subject = "Score sheet"
text_content = "This is the text version of your email."
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Email Subject</title>
</head>
<body>
    <div style="font-family: Arial, sans-serif;">
        <h1>Hello!</h1>
        <p>This is the HTML version of your email. You can customize it with your own content and styling.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor nisi nec leo auctor, id condimentum nisi sollicitudin.</p>
        <p>Nullam sit amet nulla vel nunc fermentum elementum. Integer condimentum tristique mauris, vel consectetur velit ultrices vel.</p>
        <p>Sed sit amet metus id est laoreet varius. Nam vitae nisl at urna facilisis lobortis.</p>
        <p>Regards,<br>Your Name</p>
    </div>
</body>
</html>
"""
from_email = "shivagyaneshwar06@gmail.com"
from_name = "Shiva"
to_emails = ["lavanyabk16@gmail.com"]

send_email(api_key, subject, text_content, html_content, from_email, from_name, to_emails)
