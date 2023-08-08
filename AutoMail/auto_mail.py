import os
from email.message import EmailMessage
from structure import body_structure, title_structure
import ssl
import smtplib

email_user = os.environ.get('EMAIL_USER')
email_pass = os.environ.get('EMAIL_PASS')
email_receptor = os.environ.get('EMAIL_RECEPTOR')

title = title_structure
body = body_structure

email = EmailMessage()
email["From"] = email_user
email["To"] = email_receptor
email["Subject"] = title
email.set_content(body)

context_variable = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context_variable) as smtp:
    smtp.login(email_user, email_pass)
    smtp.sendmail(email_user, email_receptor, email.as_string())
    print("Email enviado")