import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, message):
    host = "smtp.gmail.com"
    port = 465

    username = "lexure.velasco14@gmail.com"
    password = os.getenv("API_APP_PASSWORD")

    receiver = "lexure.velasco14@gmail.com"
    context = ssl.create_default_context()

    # Create email with HTML content
    email_message = MIMEMultipart("alternative")
    email_message["Subject"] = subject
    email_message["From"] = username
    email_message["To"] = receiver

    # Attach the HTML message
    html_content = MIMEText(message, "html")
    email_message.attach(html_content)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message.as_string())
