#! /usr/bin/env python
import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

with open ('password.txt' , 'r') as file:
   password = file.read()

with open ('email.txt' , 'r') as file:
   email = file.read()

with open ('text.txt' , 'r') as file:
   text = file.read()

image_file = 'final.png'
image = open (image_file,'rb')
p=MIMEBase('application','octet-stream')
p.set_payload(image.read())
encoders.encode_base64(p)
p.add_header('Content-Dispostion',f'attachment; filename = image_file')

server = smtplib.SMTP ('smtp.gmail.com', 25)
server.starttls()
server.ehlo()
server.login('pob2125@email.vccs.edu',password)

msg=MIMEMultipart()
msg['From'] = 'Bank of America'
msg['To'] = email
msg['Subject'] = 'Emergency'
msg.attach(p)
msg.attach(MIMEText(text,'plain'))

server.sendmail('pob2125@email.vccs.edu',email.split(','),msg.as_string())
