#Program to send mail
import smtplib 
   
server = smtplib.SMTP('smtp.gmail.com', 587) 

server.starttls() 

server.login("venkatesh.b.8.97@gmail.com", "aqwsderf3") 

message = """From: <venkatesh.b.8.97@gmail.com>
To: <venkateshbadarala99@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Test mail

This mail is sent through python.
"""
server.sendmail("venkatesh.b.8.97@gmail.com", "venkateshbadarala99@gmail.com", message) 
server.quit() 
