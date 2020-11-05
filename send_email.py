#Program to send mail
import smtplib 
import stdiomask
error_opening_file = 'File may not exist or error opening file.'

sender_email_address = input("Enter email address: ")
sender_email_password = stdiomask.getpass('Enter password: ', mask = '*')
receiver_address = input("Enter reciever email address: ")

try:
	with open("mail_content.txt") as f_mail_content:
		mail_content = f_mail_content.read()

except Exception:
	print(error_opening_file)

try: 
	server = smtplib.SMTP('smtp.gmail.com', 587) 
	server.starttls() 
except Exception:
	print("Error connecting to server.")


try:
	server.login(sender_email_address, sender_email_password) 
except Exception:
	print("Invalid username or password")
	exit(0)

try:
	server.sendmail(sender_email_address,receiver_address, mail_content) 
	print("Mail sent successfully.")
except Exception:
	print("Error sending mail.")
server.quit()
