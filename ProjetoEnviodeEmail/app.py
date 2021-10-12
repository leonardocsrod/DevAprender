import os
import smtplib
from email.message import EmailMessage
from segredos import senha

#configurar email, senha
EMAIL_ADRESS = 'leocesar1977@gmail.com'
EMAIL_PASSWORD = senha

#criar um e-mail
msg = EmailMessage()
msg['Subject'] = 'Carga #35 chegou ao porto'
msg['From'] = 'leocesar1977@gmail.com'
msg['To'] = 'leonardo.cesar@gmail.com'
msg.set_content('Favor buscar carga.')


#enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

