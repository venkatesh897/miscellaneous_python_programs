import requests
import json
import playsound

app_id = '46edff97'
app_key = '7031f12a59d6840a62c487f6d18f55ff'

language = 'en-gb'
word_id = input("Enter word: ")
pronunciations = 'pronunciations'
definitions = 'definitions'
strictMatch = 'false'

pronunciation_url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + pronunciations + '&strictMatch=' + strictMatch;
pronunciation_response = requests.get(pronunciation_url, headers = {'app_id': app_id, 'app_key': app_key})
json_pronunciation_response = json.loads(pronunciation_response.text)

definition_url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + definitions + '&strictMatch=' + strictMatch;
definition_response = requests.get(definition_url, headers = {'app_id': app_id, 'app_key': app_key})
json_definition_response = json.loads(definition_response.text)

pronunciation = str(json_pronunciation_response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])

definition = str(json_definition_response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])

print("The definition for word %s is %s"%(word_id, definition))
playsound.playsound(pronunciation, True)
