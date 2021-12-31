import pyttsx3
import os
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(f": {audio}")
    print("  ")
    engine.runAndWait()

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)#,timeout=1,phrase_time_limit=5
    try:
        print("Recognizing.....")
        query= r.recognize_google(audio,language='en-in')
        print(f"User Said : {query}")
    except Exception as e:
        #print(e)
        #speak("Say that again")
        return "None"
    return query


while True:

    query= TakeCommand().lower()

    if "wake up" in query:
        speak("Hello Sir")
        os.startfile("D:\\Minor Project\\jarvis_AI.py")

    else:
        print("Nothing....")