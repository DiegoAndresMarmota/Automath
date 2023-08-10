import os
from email.message import EmailMessage
from structure import body_structure, title_structure
import ssl
import smtplib
import imghdr

#Varibles de entorno
email_user = os.environ.get('EMAIL_USER')
email_pass = os.environ.get('EMAIL_PASS')
email_receptor = os.environ.get('EMAIL_RECEPTOR')

#Estructura del email
title = title_structure
body = body_structure

#Formato del email
email = EmailMessage()
email["From"] = email_user
email["To"] = email_receptor
email["Subject"] = title
email.set_content(body)

#Formato del archivo adjunto
with open("img_email.jpg", "rb") as file:
    file_data = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name

email.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)


context_variable = ssl.create_default_context()

#Conexión con el servidor y credenciales
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context_variable) as smtp:
    smtp.login(email_user, email_pass)
    smtp.sendmail(email_user, email_receptor, email.as_string())
    print("Email enviado")