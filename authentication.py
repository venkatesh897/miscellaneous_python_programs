import requests
import random

def framework_authentication():
	mobile_number = input("Enter mobile number: ")

	random_number = random.randint(1000,9999)

	response = requests.get('http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=%s&msg=%s'%(mobile_number, random_number))

	OTP = int(input("Enter OTP: "))

	if random_number != OTP:
		print("INVALID OTP")
		exit()
