#Later each command will be moved to its own py file.
#The commands will be required from their dir when needed.

#Time
from time import localtime
def Time():
    theTime = localtime()
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

#SearchOnWeb
from webbrowser import open
from urllib.parse import quote
from requests import get
try:
    from bs4 import BeautifulSoup
except:
    print("Please install bs4")
def SearchOnWeb(speech):
    searchTerm = speech.split()[2:]
    if speech.endswith("online"):
        open("https://www.google.com/search?q=" + quote(" ".join(searchTerm[:-1])))
        return "Searching for " + " ".join(searchTerm)
    elif speech.endswith("on youtube"):
        response = get("https://www.youtube.com/results?search_query=" + quote(" ".join(searchTerm[:-2])))
        soup = BeautifulSoup(response.text, "html.parser")
        for i in soup.findAll(attrs={"class":"yt-uix-tile-link"})[:3]:
            #later, make the Assistant say the title, the user can repeat it/a number and it will open
            #Try to remove google ads if possible
            print(i["title"])
            print("https://www.youtube.com" + i["href"])
