'''
Tumblr Archive Image Scraper
Scrape and save all the images from a given tubmlr blog archive page (without the Tumblr api).
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from bs4 import BeautifulSoup

def connect(url):
    headers = { 'User-Agent' : 'Mozilla/5.0' }

    with urllib.request.urlopen(urllib.request.Request(url, None, headers)) as url:
        page = url.read()

    return page

def save_images(link_list):

    for link in link_list:
        page = connect(link)
        soup = BeautifulSoup(page, "html.parser")
        images = soup.find_all("img")

        for img in images:
            image = img.get("src")
            image_name = image.split("/")[-1]
            if "tumblr" in image_name:
                urllib.request.urlretrieve(image, image_name)
                print(image_name + " saved.")

def pull_images(page):
    link_list = []
    soup = BeautifulSoup(page, "html.parser")
    links = soup.find_all("a")

    for link in links:
        url = link.get("href")
        if url not in link_list:
            if "http" in url:
                link_list.append(url.replace("/post/", "/image/"))

    save_images(link_list)

def connect_tumblr(url):
    browser = webdriver.Chrome()
    browser.get(url)
    return browser

def get_links(url):
    browser = connect_tumblr(url)

    #spawn lazy load images
    SCROLL_PAUSE_TIME = 1.5
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")

        #lazy load finish
        if new_height == last_height:
            pull_images(browser.page_source)
            browser.quit()

        last_height = new_height

url = "tumblr image archive url"
get_links(url)
