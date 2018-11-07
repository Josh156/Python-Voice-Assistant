print("Starting...")

#Import necessary libraries.
from win32com.client import Dispatch
from webbrowser import open
from datetime import datetime
try:
    import speech_recognition as sr
except:
    print("Please install SpeechRecognition and PyAudio!")

#Import commands.
import CMDS

#Start up TTS libraries.
speak = Dispatch("SAPI.SpVoice")
def tts(string):
    if string != None:
        speak.Speak(string)#Change the voice so it doesnt sound like a thot.

#Extract what's needed from play and search commands.
def extract(results):
    if type(results) == tuple:
        tts(results[0])
        tts("Which would you like to select; 1, 2, or 3?")
        speech = listen()
        if type(speech) != None:#speech.isdigit() and type(speech) != None:
            try:
                open(results[1][int(speech) - 1])
            except:
                pass
    else:
        tts(results)

#Triggers when the user speaks.
def userSpoke(speech):
    if speech != None:
        print(speech)
        #Time
        if speech == "what's the time" or speech == "what is the time":
            tts(CMDS.Time())
        #Play
        elif speech.startswith("play"):
            extract(CMDS.Play(speech))
        #Search
        elif speech.startswith("search for"):
            extract(CMDS.Search(speech))
        #Some Fortnite meme
        elif speech == "fortnite" or speech == "fortnight":
            tts("Fortnite players are virgins, by the way fortnight dances are pretty cool!")
        #github repo
        elif speech == "open your github repository":
            open("https://github.com/Josh1560/Python-Voice-Assistant")
        #date
        elif speech == "what's the date" or speech == "what is the date":
            tts(CMDS.Date())
        elif speech == "what's the weather" or speech == "what is the weather" or speech == "what is the weather like" or speech == "what's the weather like":
            tts(CMDS.CW())
        else:
            tts("I'm sorry, I didn't recognise that command.")

#Does the SpeechRecognition stuff
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            return(r.recognize_google(audio))
        except:
            tts("I couldn't quite catch that")

#Later we will change this to a phrase like "okay, python"
while True:
    userInput = input("Would you like me to listen? (y/n)\n")
    if userInput == "y":
        userSpoke(listen())
    if userInput == "n":
        quit()
