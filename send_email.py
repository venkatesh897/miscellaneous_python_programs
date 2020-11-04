#Program to send mail
import smtplib 
import getpass
error_opening_file = 'File may not exist or error opening file.'

sender_email_address = input("Enter email address: ")
sender_email_password = getpass.getpass('Enter password: ')
receiver_address = input("Enter reciever email address: ")

try:
	with open("mail_content.txt") as f_mail_content:
		mail_content = f_mail_content.read()

except Exception:
	print(error_opening_file)
   
server = smtplib.SMTP('smtp.gmail.com', 587) 

server.starttls() 

server.login(sender_email_address, sender_email_password) 

server.sendmail(sender_email_address,receiver_address, mail_content) 
server.quit() 
