import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email(subject, to_email, cc_email=None, bcc_email=None, props=None, template_path=None, entity_category=None, attachment_file=None):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'shivagyaneshwar06@gmail.com'
    smtp_password = 'gknmkketclvabaxd'

    # Sender email address based on entity category
    if entity_category == 'SOCIETY':
        from_email = 'from_societies_email@example.com'
    else:
        from_email = 'from_professionals_email@example.com'

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    if cc_email:
        msg['Cc'] = cc_email
    if bcc_email:
        msg['Bcc'] = bcc_email
    msg['Subject'] = subject

    # Email content
    if template_path:
        with open(template_path, 'r') as template_file:
            email_content = template_file.read()
    else:
        email_content = ''

    # Attach email content
    msg.attach(MIMEText(email_content, 'html'))

    # Attach file if provided
    if attachment_file:
        attachment = MIMEApplication(open(attachment_file, 'rb').read())
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_file))
        msg.attach(attachment)

    # Sending email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

    # Delete attachment file if provided
    # if attachment_file:
    #     os.remove(attachment_file)

# Example usage
send_email("Hello", "lavanyabk16@gmail.com", cc_email="kg3734@srmist.edu.in", bcc_email="shivadevops253@gmail.com", template_path="E:\wati testing\basic.html", entity_category="SOCIETY", attachment_file=r"C:\Users\shiva\Downloads\Workitems-Tracker-Template.xlsx")
