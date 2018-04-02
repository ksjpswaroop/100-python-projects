#RSS Feed Creator - Given a link to RSS/Atom Feed, get all posts and display them.
import urllib.request
from bs4 import BeautifulSoup

headers = { 'User-Agent' : 'Mozilla/5.0' }
URL = "given url"
page = urllib.request.Request(URL, None, headers)
page = urllib.request.urlopen(page)
data = page.read()
page.close()

def parse(data):
    soup = BeautifulSoup(data, features='xml')
    entries = soup.find_all('entry')
    items = soup.find_all('item')
    if entries:
        for entry in entries:
            print(entry.title.text)
            print(entry.link.get('href'))
            print('\n')
            if entry.summary:
                print(entry.summary.text + '\n')
            elif entry.content:
                print(entry.content.text + '\n')
    elif items:
        for item in items:
            print(item.title.text)
            print(item.link.text)
            print('\n')
            if item.description:
                print(item.description.text + '\n')

parse(data)
