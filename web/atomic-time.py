'''
Get Atomic Time from Internet Clock
This program will get the true atomic time from an atomic time clock on the Internet. Use any one of the atomic clocks returned by a simple Google search.
'''
import urllib.request
from bs4 import BeautifulSoup

def connect(url):
    headers = { 'User-Agent' : 'Mozilla/5.0' }

    with urllib.request.urlopen(urllib.request.Request(url, None, headers)) as url:
        page = url.read()

    return page


def get_time(url):
    page = connect(url)
    
    soup = BeautifulSoup(page, "lxml")
    time = soup.find("div", {"id": "i_time"})

    return time.text

url = "https://www.timeanddate.com/worldclock/fullscreen.html?n=4757"
print(get_time(url))
