#Later each command will be moved to its own py file.
#Commands that require the same libraries will be put together
#The commands will be required from their dir when needed.

#Date
#you should track your date and not ask a robot to tell you what the date is
from time import localtime
def Date():
    theTime = localtime()
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthDay = theTime[2]
    if monthDay == 1:
        date = "first"
    elif monthDay == 2:
        date = "second"
    elif monthDay == 3:
        date = "third"
    else:
        if monthDay > 20:
            if str(monthDay)[-1] == "1":
                date = str(round(monthDay, -1)) + " first"
            elif str(monthDay)[-1] == "2":
                date = str(round(monthDay, -1)) + " second"
            elif str(monthDay)[-1] == "3":
                date = str(round(monthDay, -1)) + " third"
            else:
                date = str(monthDay) + "th"
        else:
            date = str(monthDay) + "th"
    return("Today is, " + day_list[theTime[6]] + ", the " + date + " of " + month_list[theTime[1] - 1])

#Time
#Finish off testing this feature
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

#theWeather
#uses your ip to get your approximate geolocation to give the correct weather status
from json import loads
try:
    from weather import Weather, Unit
except:
    print("Please install weather-api!")
def theWeather():
    response = get("http://ipinfo.io/json")
    responseDecode = loads(response.text)
    latlon = responseDecode["loc"].split(",")
    weather = Weather(unit=Unit.CELSIUS)
    lookup = weather.lookup_by_latlng(latlon[0], latlon[1])
    condition = lookup.condition
    #print("Currently, in " + responseDecode["city"] + " it is " + condition.temp + " degrees")
    return("Currently, in " + responseDecode["city"] + " it is " + condition.temp + " degrees")
