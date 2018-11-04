print("Starting...")

#import
from win32com.client import Dispatch
import speech_recognition as sr
import time

#make tts speak
speak = Dispatch("SAPI.SpVoice")
def tts(string):
    speak.Speak(string)

#userspoke function
def userSpoke(speech):
    print(speech)
    if speech == "what's the time": #try to make this say things like 5 past 1
        theTime = time.localtime()#[0, 0, 0, 1, 0]
        if theTime[3] > 12:
            hour = str(theTime[3] - 12)
        else:
            hour = str(theTime[3])
        if theTime[4] < 10:
            if theTime[4] == 0:
                minute = "o'clock"
            else:
                minute = "0" + str(theTime[4])
        else:
            minute = str(theTime[4])
        tts("The time is " + hour + " " + minute)
        print(hour, minute)

#speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        #try:
        userSpoke(r.recognize_google(audio))
        #except:
            #tts("I couldn't quite catch that")

#wait for the user to give microphone permission
#later we will change this to a phrase like "okay, python"
while True:
    userInput = input("Would you like me to listen? (y/n)\n")
    if userInput == "y":
        listen()
