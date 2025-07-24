import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)
