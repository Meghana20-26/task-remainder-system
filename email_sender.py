import smtplib
from email.mime.text import MIMEText

def send_email(to_email, task_name):

    sender = "your_email@gmail.com"
    password = "your_app_password" 
    
    subject = "Task Remainder"
    message = f"Remainder: your task'{task_name}' deadline is approaching."

    msg = MIMEText(message)
    msg["subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(sender, password)

    server.sendmail(sender, to_email, msg.as_string())

    server.quit()