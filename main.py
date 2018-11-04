print("Starting...")

#import
from win32com.client import Dispatch
import speech_recognition as sr #pip install SpeechRecognition/PyAudio
import time

#make tts speak
speak = Dispatch("SAPI.SpVoice")
def tts(string):
    speak.Speak(string)

#userspoke function
def userSpoke(speech):
    print(speech)
    #try to make this say things like 5 past 1
    if "what's the time" or "what is the time" in speech :#speech == "what's the time" or speech == "what is the time":
        theTime = time.localtime()#[0, 0, 0, 1, 15]

        #convert military time
        if theTime[3] > 12:
            hour = str(theTime[3] - 12)
        else:
            hour = str(theTime[3])

        #decide past or to
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

        #send arguments to function
        tts("The time is " + arguments)
        #print(arguments)

#speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        r.energy_threshold = 5000
        try:
            userSpoke(r.recognize_google(audio))
        except:
            tts("I couldn't quite catch that")

#wait for the user to give microphone permission
#later we will change this to a phrase like "okay, python"
#userSpoke("what's the time")
while True:
    userInput = input("Would you like me to listen? (y/n)\n")
    if userInput == "y":
        listen()
    if userInput == "n":
        quit()
