import os
from email.message import EmailMessage

email_user = os.environ.get('EMAIL_USER')
email_pass = os.environ.get('EMAIL_PASS')
email_receptor = os.environ.get('EMAIL_RECEPTOR')

title = "Asunto: Respuesta a su consulta / Solicitud de información"
body = """Estimado/a [Nombre del Cliente/Formal]:

Espero que este correo lo encuentre bien. En nombre de [Nombre de la Institución/Compañía], me complace responder a su consulta / solicitud de información que recibimos recientemente.

Antes que nada, queremos expresar nuestro agradecimiento por su interés en nuestros productos / servicios y por tomar el tiempo para ponerse en contacto con nosotros.

[En esta sección, es importante ser claro y conciso al proporcionar la información solicitada por el cliente. Si es necesario, incluya detalles técnicos o aspectos específicos relacionados con la consulta del cliente. Si la consulta requiere investigación adicional, asegúrese de mencionar que están trabajando en ello y proporcionará una respuesta completa lo antes posible.]

Si tiene alguna otra pregunta o inquietud, no dude en hacérnoslo saber. Estamos aquí para ayudarle en todo lo que podamos.

[Si corresponde, agregue una breve mención sobre la política de privacidad o términos y condiciones aplicables.]

Nuevamente, agradecemos su interés en [Nombre de la Institución/Compañía] y esperamos poder servirle de la mejor manera posible. Si necesita más asistencia, no dude en comunicarse con nuestro equipo de soporte.

Atentamente,

[Su Nombre]
[Su Cargo/Posición]
[Nombre de la Institución/Compañía]
[Teléfono de Contacto]
[Correo Electrónico de Contacto]"""

email = EmailMessage()
email["from"] = email_user
email["to"] = email_receptor