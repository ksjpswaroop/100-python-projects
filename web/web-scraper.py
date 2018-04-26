'''
Page Scraper - Create an application which connects to a site and pulls out all links, or images, and saves them to a list. Optional: Organize the indexed content and don’t allow duplicates. Have it put the results into an easily searchable index file.
'''
import urllib.request
from bs4 import BeautifulSoup

def connect(url):
    headers = { 'User-Agent' : 'Mozilla/5.0' }

    with urllib.request.urlopen(urllib.request.Request(url, None, headers)) as url:
        page = url.read()

    return page


def pull_links(url):
        page = connect(url)
        url_list = []

        soup = BeautifulSoup(page, "lxml")
        links = soup.find_all("a")

        for link in links:
            url = link.get("href")
            if url not in url_list:
                if "http" in url or "www" in url:
                    url_list.append(url)
        print(url_list)


def pull_images(url):
    page = connect(url)
    image_list = []

    soup = BeautifulSoup(page, "lxml")
    images = soup.find_all("img")

    for img in images:
        image = img.get("src")
        if image not in image_list:
            image_list.append(image)
    print(image_list)

url = ""
pull_links(url)
pull_images(url)
