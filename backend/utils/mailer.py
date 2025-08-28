import os
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # `html=True` -> send as HTML, else plain text
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = os.getenv('EMAIL_HOST_USER')
    msg["To"] = to_email

    with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT", 587))) as server:
        server.starttls()
        server.login(
            os.getenv("EMAIL_HOST_USER"),
            os.getenv("EMAIL_HOST_PASSWORD")
        )
        server.send_message(msg)
