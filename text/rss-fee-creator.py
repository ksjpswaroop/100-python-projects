#RSS Feed Creator - Given a link to RSS/Atom Feed, get all posts and display them.
import urllib.request
from bs4 import BeautifulSoup

headers = { 'User-Agent' : 'Mozilla/5.0' }
URL = "https://medialibre.net/feed/atom/"
page = urllib.request.Request(URL, None, headers)
page = urllib.request.urlopen(page)
data = page.read()
page.close()

def parse(data):
    soup = BeautifulSoup(data, features='xml')
    entries = soup.find_all('entry')
    for entry in entries:
        print(entry.title.text)
        print(entry.id.text)
        print('\n')
        if (entry.summary.text):
            print(entry.summary.text + '\n')

parse(data)
