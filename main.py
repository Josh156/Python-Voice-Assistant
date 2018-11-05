print("Starting...")

#Import necessary libraries.
from win32com.client import Dispatch
import time, webbrowser
from urllib.parse import quote

try:
    import speech_recognition as sr
except:
    print("Please install SpeechRecognition and PyAudio!")

#Start up TTS libraries.
speak = Dispatch("SAPI.SpVoice")
def tts(string):
    speak.Speak(string)

#Triggers when the user speaks.
def userSpoke(speech):
    print(speech)
    #Time
    if "what's the time" in speech or "what is the time" in speech:
        theTime = time.localtime()
        if theTime[3] > 12:
            hour = str(theTime[3] - 12)
        else:
            hour = str(theTime[3])
        minute = theTime[4]
        if minute > 30:
            hour = str(int(hour) + 1)
            if minute == 45:
                arguments = "quarter to " + hour
            else:
                arguments = str(60 - minute) + " minutes to " + hour
        else:
            if minute == 0:
                arguments = hour + " o'clock"
            elif minute == 15:
                arguments = "quarter past " + hour
            elif minute == 30:
                arguments = "half past " + hour
            else:
                arguments = str(minute) + " minutes past " + hour
        tts("The time is " + arguments)
    #Search Online
    elif speech.startswith("search for"):
        searchTerm = speech.split()[2:]
        #webbrowser.open("https://www.bing.com/search?q=" + "PUT STUFF HERE" + "&qs=n&form=QBLH&sp=-1&pq=&sc=0-0&sk=&cvid=A033E86F19034F1AB1319EADE113793B")
        if speech.endswith("online"):
            webbrowser.open("https://www.google.co.uk/search?q=" + quote(" ".join(searchTerm[:-1])))
        elif speech.endswith("on youtube"):
            tts("This feature is coming soon...")
    #Some Fortnite meme
    elif "fortnite" in speech:
        tts("Fortnite players are virgins, by the way fortnight dances are pretty cool!")

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
