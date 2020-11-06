import speech_recognition
import pyttsx3


def text_to_speech():
    speaker = pyttsx3.init()
    text = input("Enter text: ")
    try:
        speaker.say(text)
        speaker.runAndWait()
    except Exception:
        print("Error speaking text.")


def speech_to_text():
    recognize = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Start speaking: ")
        audio_text = recognize.record(source, duration = 10)
        print("Time's up")
     
    try:
        print("Text: "+recognize.recognize_google(audio_text))
    except Exception:
        print("Sorry, I did not get that")



try:
    with open("speech_text_menu.cfg") as f_fields:
        menu = f_fields.read()
except Exception:
    print("Error opening file or file may not exist.")

function_list = [speech_to_text, text_to_speech, exit]

while True:
    print(menu)
    user_input = int(input("Enter option: "))
    function_list[user_input - 1]()
