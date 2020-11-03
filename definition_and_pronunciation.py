#Program to print definition and play pronunciation of a word
import requests
import json
import playsound

app_id = '46edff97'
app_key = '7031f12a59d6840a62c487f6d18f55ff'

try:
  word_id = argv[1]
except Exception:
  word_id = input("Enter word: ")
language = 'en-gb'
pronunciations = 'pronunciations'
definitions = 'definitions'
strictMatch = 'false'

url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower()
response = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
json_response = json.loads(response.text)

pronunciation = str(json_response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])

definition = str(json_response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])

print("The definition for word %s is %s"%(word_id, definition))
playsound.playsound(pronunciation, True)
