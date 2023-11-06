import smtplib
import ssl
from email.message import EmailMessage

subject= "Python test email"

body= "sending email from python"

sender_email="linabousbih@gmail.com"
receiver_email="nad.cheikhrouhou@gmail.com"
password=input("Your password : ")

message=EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]=subject
message.set_content(body)


html=f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    <body>
<html>
"""
context=ssl.create_default_context()
message.add_alternative(html,subtype="html")

print("Sending Email...")

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("Email sent!")