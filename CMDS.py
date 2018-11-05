from win32com.client import Dispatch
import time, webbrowser
from urllib.parse import quote

def Time():
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
    return "The time is " + arguments

def SearchOnWeb(speech):
    searchTerm = speech.split()[2:]
    if speech.endswith("online"):
        webbrowser.open("https://www.google.com/search?q=" + quote(" ".join(searchTerm[:-1])))
