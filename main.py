print("Starting...")

#Import necessary libraries.
from win32com.client import Dispatch
from webbrowser import open
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
    if speech != None:
        print(speech)
        #Time
        if "what's the time" in speech or "what is the time" in speech:
            tts(CMDS.Time())
        #SearchOnWeb
        elif speech.startswith("search for"):
            results = CMDS.SearchOnWeb(speech)
            #THE FOLLOWING FEW LINES ARE A PAIN IN THE ASS
            #Basically more efficient, but more likely to crash and burn
            if type(results) == tuple:
                tts(results[0])
                tts("Which would you like to select; 1, 2, or 3?")
                speech = listen()
                if speech.isdigit():
                    try:
                        open(results[1][int(speech) - 1])
                    except:
                        pass
            else:
                tts(results)
        #Some Fortnite meme
        elif speech == "fortnite" or speech == "fortnight":
            tts("Fortnite players are virgins, by the way fortnight dances are pretty cool!")
        #github repo
        elif speech == "open your github repository":
            webbrowser.open("https://github.com/Josh1560/Python-Voice-Assistant")

#Does the SpeechRecognition stuff
#change this to a  return so it's a little more flexible
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
        #userSpoke("search for remember the name on youtube")
        #userSpoke("what is the time")
        #userSpoke("search for michael reeves online")
    if userInput == "n":
        quit()
