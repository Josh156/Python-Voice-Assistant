print("Starting...")

#Import necessary libraries.
from win32com.client import Dispatch
try:
    import speech_recognition as sr
except:
    print("Please install SpeechRecognition and PyAudio!")

#Import commands.
import CMDS

#Start up TTS libraries.
speak = Dispatch("SAPI.SpVoice")
def tts(string):
    speak.Speak(string)#make it not sound like a th0t

#Triggers when the user speaks.
def userSpoke(speech):
    print(speech)
    #Time
    if "what's the time" in speech or "what is the time" in speech:
        tts(CMDS.Time())
    #SearchOnWeb
    elif speech.startswith("search for"):
        tts(CMDS.SearchOnWeb(speech))
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
        #userSpoke("search for remember the name on youtube")
        #userSpoke("search for william osman on youtube")
        #userSpoke("search for michael reeves on youtube")
    if userInput == "n":
        quit()













#hmm
