'''
Fetch Current Weather
Locate the user automatically and get the current weather.
'''
import urllib.request
import json
import geocoder

def connect(url):
    headers = { 'User-Agent' : 'Mozilla/5.0' }

    with urllib.request.urlopen(urllib.request.Request(url, None, headers)) as url:
        page = url.read()
        data = json.loads(page.decode())

    return data

def get_weather(url):
    #get lat and long
    g = geocoder.ip('me')
    url = url + "lat=" + str(g.lat) + "&lon=" + str(g.lng)

    page = connect(url)

    print("Weather: {}".format(page["weather"][0]["description"]))
    print("Temprature: {}".format(page["main"]["temp"]))


#freecodecamp weather api
url = "https://fcc-weather-api.glitch.me/api/current?"
get_weather(url)
