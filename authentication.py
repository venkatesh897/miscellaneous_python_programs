#Generate OTP and validate
import requests
import random
import sys

def framework_authentication():
	try:
		mobile_number = sys.argv[1]
	except Exception:
		mobile_number = input("Enter mobile number: ")

	random_number = random.randint(1000,9999)

	response = requests.get('http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=%s&msg=%s'%(mobile_number, random_number))

	OTP = int(input("Enter OTP: "))

	if random_number != OTP:
		print("INVALID OTP")
		exit()
