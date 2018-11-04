print("Starting...")

#import
from win32com.client import Dispatch
import speech_recognition as sr #pip install SpeechRecognition/PyAudio
import time
import webbrowser

#make tts speak
speak = Dispatch("SAPI.SpVoice")
def tts(string):
    speak.Speak(string)

#userspoke function
def userSpoke(speech):
    print(speech)
    #try to make this say things like 5 past 1
    if "what's the time" in speech or "what is the time" in speech:
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
    elif speech == "fortnite players are":
        tts("Virgins")
        tts("By the way fortnight dances are pretty cool!")
    elif speech == "search for " + speech.split()[2] + " online":
        webbrowser.open_new("https://www.bing.com/search?q=" + speech.split()[2] + "&qs=n&form=QBLH&sp=-1&pq=&sc=0-0&sk=&cvid=A033E86F19034F1AB1319EADE113793B")

#speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
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
