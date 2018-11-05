print("Starting...")

#Import necessary libraries.
from win32com.client import Dispatch
import time, webbrowser
from urllib.parse import quote

import CMDS

try:
    import speech_recognition as sr
except:
    print("Please install SpeechRecognition and PyAudio!")

try:
    from bs4 import BeautifulSoup
except:
    print("Please install bs4")

#Start up TTS libraries.
speak = Dispatch("SAPI.SpVoice")
def tts(string):
    speak.Speak(string)

#Triggers when the user speaks.
def userSpoke(speech):
    print(speech)
    #Time
    if "what's the time" in speech or "what is the time" in speech:
        CMDS.Time()
    #Search Online
    elif speech.startswith("search for"):
        if True:
            print("Hello World!")
            #search online code was moved to CMDS.py
        elif speech.endswith("on youtube"):
            #tts("This feature is coming soon!")

            print("Lotta testing")
    #Some Fortnite meme
    elif speech == "fortnite" or speech == "fortnight":
        tts("Fortnite players are virgins, by the way fortnight dances are pretty cool!")
    #github repo
    elif speech == "open your github repository":
        webbrowser.open("https://github.com/Josh1560/Python-Voice-Assistant")

#Does the SpeechRecognition stuff
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        #try:
        userSpoke(r.recognize_google(audio))
        #except:
            #tts("I couldn't quite catch that")

#Later we will change this to a phrase like "okay, python"
while True:
    userInput = input("Would you like me to listen? (y/n)\n")
    if userInput == "y":
        listen()
        #userSpoke("search for huhehu online")
    if userInput == "n":
        quit()

#hmm
