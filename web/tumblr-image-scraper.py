'''
Tumblr Image Scraper
Scrape all the images from a given tubmlr blog page (with a Tumblr api key).
'''
import time
import urllib.request
import json

URL = "https://api.tumblr.com/v2/blog/[tumblr blog url]/posts/photo?api_key=[api key]&limit=50"

def connect(url):
    headers = { 'User-Agent' : 'Mozilla/5.0' }

    with urllib.request.urlopen(urllib.request.Request(url, None, headers)) as url:
        page = url.read()
        data = json.loads(page.decode())

    return data

def scrape_images(url_offset, offset):
    data = connect(url_offset)
    print(url_offset, offset)
    total_posts = data['response']['total_posts']

    #if  posts still left
    if offset < total_posts:

        count = len(data["response"]["posts"])
        for i in range(count):
            image = data["response"]["posts"][i]["photos"][0]["original_size"]["url"]
            image_name = image.split("/")[-1]
            urllib.request.urlretrieve(image, "image_folder/" + image_name)
            print(image_name + " saved.")

        offset += 50
        url_offset = URL + "&offset=" + str(offset)

        #call the function again
        scrape_images(url_offset, offset, posts_still_left)

offset = 0
scrape_images(URL, offset)
