print("Starting...")

#Import necessary libraries.
from win32com.client import Dispatch
import time, webbrowser
from urllib.parse import quote

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
        
    #Search Online
    elif speech.startswith("search for"):
        searchTerm = speech.split()[2:]
        #webbrowser.open("https://www.bing.com/search?q=" + "PUT STUFF HERE" + "&qs=n&form=QBLH&sp=-1&pq=&sc=0-0&sk=&cvid=A033E86F19034F1AB1319EADE113793B")
        if speech.endswith("online"):
            webbrowser.open("https://www.google.com/search?q=" + quote(" ".join(searchTerm[:-1])))
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
        try:
            userSpoke(r.recognize_google(audio))
        except:
            tts("I couldn't quite catch that")

#Later we will change this to a phrase like "okay, python"
while True:
    userInput = input("Would you like me to listen? (y/n)\n")
    if userInput == "y":
        listen()
        #userSpoke("search for huhehu online")
    if userInput == "n":
        quit()

#hmm
