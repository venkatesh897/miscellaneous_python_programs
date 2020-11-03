#Program to generate OTP
import requests
import random

def framework_authentication():
	try:
		mobile_number = argv[1]
	else:
		mobile_number = input("Enter mobile number: ")

	random_number = random.randint(1000,9999)

	response = requests.get('http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=%s&msg=%s'%(mobile_number, random_number))

	OTP = int(input("Enter OTP: "))

	if random_number == OTP:
		print("Access granted.")
	else:
		print("Access denied.")
		
framework_authentication()
