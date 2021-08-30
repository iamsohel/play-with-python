from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
import smtplib

template = Template(Path("standard_lib/email_template.html").read_text())

message = MIMEMultipart()
message['from'] = 'sohel rana'
message['to'] = 'sohelcuetcse11@gmail.com'
message['subject'] = 'Python Playground'
body = template.substitute({"name": "Sohel"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("sohel.jpg").read_bytes(), _subtype="jpeg"))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(message)
    print("sent...")
