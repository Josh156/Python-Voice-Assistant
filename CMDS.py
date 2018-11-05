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
#try to make it so people dont accidentally say bad words and get arrested by the FBI guy
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
        videos = soup.findAll(attrs={"class":"yt-uix-tile-link"})[1:4]
        #Was [:3], changed to [1:4] to try to stop ads
        #Try to remove google ads if possible (May have fixed, but test this)
        #Try to filter out channels, not sure if it's happening or not though
        #Later, make the user repeat the name or a number and it will open
        names = list()
        links = list()
        for i in range(len(videos)):
            #print(videos[i]["title"])
            names.insert(i, videos[i]["title"])
            #print(videos[i]["href"])
            links.insert(i, "https://www.youtube.com" + videos[i]["href"])
        #test = ",".join(findall)
        print("I found 3 videos, " + ", ".join(names))
        return "I found 3 videos, " + ", ".join(names)
