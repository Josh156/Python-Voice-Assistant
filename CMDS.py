#Later each command will be moved to its own py file.
#Commands that require the same libraries will be put together
#The commands will be required from their dir when needed.

#Time
#Finish off testing this feature
from time import localtime
from datetime import datetime
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
    return("The time is " + arguments)

#Play
from webbrowser import open
from urllib.parse import quote
from requests import get
try:
    from bs4 import BeautifulSoup
except:
    print("Please install bs4!")
def Play(speech):
    if speech.endswith("on YouTube"):
        searchTerm = speech.split()[1:]
        response = get("https://www.youtube.com/results?search_query=" + quote(" ".join(searchTerm[:-2])))
        soup = BeautifulSoup(response.text, "html.parser")
        videos = soup.findAll(attrs={"class":"yt-uix-tile-link"})[1:4]
        #Was [:3], changed to [1:4] to try to stop ads
        #Try to remove google ads if possible (May have fixed, but test this)
        names = list()
        links = list()
        for i in range(len(videos)):
            names.insert(i, videos[i]["title"])
            links.insert(i, "https://www.youtube.com" + videos[i]["href"])
        return("I found 3 videos. " + ". ".join(names), links)

#Search
#try to make it so people dont accidentally say bad words and get arrested by the FBI guy
def Search(speech):
    searchTerm = speech.split()[2:]
    if speech.endswith("online"):
        open("https://www.google.com/search?q=" + quote(" ".join(searchTerm[:-1])))
        return("Searching for " + " ".join(searchTerm))
    elif speech.endswith("on YouTube"):
        return(Play(speech[6:]))

#Date
#for all of the faggits that dont track their date, jk i dont track the date myself
def Date():
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    raw_date = str(datetime.today()).split()[0]
    date = raw_date.split("-")
    day = day_list[int(datetime.today().weekday())-1]
    month = month_list[int(datetime.today().month)-1]
    if day == day_list[0]:
        tts_data = "Today is {}, first {} {}".format(day, month_list[int(date[1])], date[0])
        return tts_data
    elif day == day_list[1]:
        tts_data = "Today is {}, second {} {}".format(day, month_list[int(date[1])], date[0])
        return tts_data
    elif day == day_list[2]:
        tts_data = "Today is {}, third {} {}".format(day, month_list[int(date[1])], date[0])
        return tts_data
    else:
        tts_data = "Today is {}, {}th {} {}".format(day, date[2], month_list[int(date[1])], date[0])
        return tts_data
