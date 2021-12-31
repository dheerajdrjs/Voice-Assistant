#J.A.R.V.I.S (Just A Rather Very Intelligent System)

import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import random
import subprocess
from requests import get
import pywhatkit as kit
import pyautogui
import smtplib
import sys




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
 
#to wish   
def WishMe():
    
    hour=int(datetime.datetime.now().hour)
    if(hour>0 and hour<12):
        speak("Good Morning!")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the time is {time}")
    speak("My name is jarvis, tell me how can i help you")

#to convert voice to text
def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query= r.recognize_google(audio,language='en-in')
        print(f"User Said : {query}")
    except Exception as e:
        #print(e)
        speak("Say that again")
        return "None"
    return query

def Send_Email(to,subject):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("sharmadheerajkumar517@gmail.com","8271137764")
    server.sendmail("sharmadheerajkumar517@gmail.com", to, subject)
    server.close()

def TaskExe():

    speak("Hi Dheeraj and Ayushi , How are you?")
    WishMe()
    while 1:

        query=TakeCommand().lower()
        
        #Open word
        if "open word" in query:
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
            speak("please wait")
            os.startfile(path)

        #Close word
        elif"close word" in query:
            speak("ok sir")
            os.system("TASKKILL /F /im WINWORD.exe")

            
        #Open VS Code   
        elif"open code" in query:
            path="C:\\Users\\dheer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Ok")
            os.startfile(path)

        #Close VS Code
        elif"close code" in query:
            speak("ok sir")
            os.system("taskkill /f /im Code.exe")
            
        #Open Command Prompt    
        elif "open command prompt" in query:
            speak("ok sir")
            os.system("start cmd")

        #Close Command Prompt
        elif "close command prompt" in query:
            speak("ok sir")
            os.system("taskkill /f /im cmd.exe")

        #Open Calculator
        elif"open calculator" in query:
            speak("ok sir")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

         #Close Calculator
        elif"close calculator" in query:
            speak("ok sir")
            os.system("TASKKILL /F /im Calculator.exe")
        
        #Open Notepad    
        elif "open notepad" in query:
            path="C:\\WINDOWS\\system32\\notepad.exe"
            speak("opening notepad")
            os.startfile(path)

        #Close Notepad
        elif"close notepad" in query:
            speak("ok sir")
            os.system("TASKKILL /F /im notepad.exe")
            
        #Open Google    
        elif"open google" in query:
            webbrowser.open("www.google.co.in")

        #Open Chrome
        elif"open chrome" in query:
            path=("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            speak("ok sir")
            os.startfile(path)
        
        #Close Chrome
        elif"close chrome" in query:
            speak("ok sir")
            os.system("taskkill /f /im chrome.exe")
            speak("closed")
        
        #Close Web Browser
        elif"close web browser" in query:
            speak("ok sir")
            os.system("taskkill /f /im msedge.exe")

        #Search on Google
        elif"search on google" in query:
            speak("what should i search on google")
            cm=TakeCommand().lower()
            speak("ok sir")
            webbrowser.open(f"{cm}")
        
        #Open Youtube
        elif"open youtube" in query:
            speak("ok sir")
            webbrowser.open("www.youtube.com")

        #Play music on youtube
        elif("on youtube" or "play music on youtube") in query:
            speak("ok, tell me which song do you want to play")
            s=TakeCommand().lower()
            speak("ok sir")
            kit.playonyt(s)

        #Open Geeksforgeeks
        elif"geeks for geeks" in query:
            speak("ok sir")
            webbrowser.open("www.geeksforgeeks.com")

        #Open StackOverFlow
        elif"stack overflow" in query:
            speak("ok sir")
            webbrowser.open("https://stackoverflow.com/")
            
        #Search on Wikipedia
        elif"search on wikipedia" in query:    #example search on wikipedia who is .......?
            speak("searching")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            print(result)
            speak(result)
        
        #Play audio file
        elif"play music" in query:
            music_dir="D:\\Minor Project\\music"
            speak("please wait")
            songs=os.listdir(music_dir)
            song=random.choice(songs)
            os.startfile(os.path.join(music_dir,song))

        #Close Music
        elif"close music" in query:
            speak("ok")
            os.system("taskkill /f /im Music.UI.exe")
        
        #Play video file
        elif"play video" in query:
            video_dir="D:\\Minor Project\\video"
            speak("please wait")
            videos=os.listdir(video_dir)
            video=random.choice(videos)
            os.startfile(os.path.join(video_dir,video))

        #Close Video Music
        elif"close video" in query:
            speak("ok sir")
            os.system("taskkill /f /im Video.UI.exe")
        
        #Volume Up
        elif"volume up" in query:
            pyautogui.press("volumeup")

        #Volume Down
        elif"volume down" in query:
            pyautogui.press("volumedown")
        
        #Volume Mute
        elif"mute" in query:
            pyautogui.press("volumemute")

        #Check IP Address
        elif"ip address" in query:
            ip=get("https://api.ipify.org").text
            print(ip)
            speak(f"your ip address is {ip}")

        #Send Email
        elif"send email" in query:
            try:
                speak("Enter receiver email id")
                to=input(": ")
                speak("what should i say?")
                subject=TakeCommand().lower()
                Send_Email(to,subject)
                speak("email has been sent")
            
            except Exception as e:
                speak("sorry sir i am not able to send this email")

        #Time
        elif"time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"the time is {time}")

        
        #For terminate this program 
        elif"no thanks"in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        elif"take a break" in query:
            speak("ok sir")
            speak("i am here for you, you can call me anytime")
            break
            
        

        speak("Sir, do you have any other work")
TaskExe()