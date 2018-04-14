'''
Site Checker with Time Scheduling
An application that attempts to connect to a website or server every
so many minutes or a given time and check if it is up.If it is down,
it will notify you by email or by posting a notice on screen.
'''
import urllib.request
import time


def connect(website, every):
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    while True:
        try:
            with urllib.request.urlopen(urllib.request.Request(website, None, headers)) as url:
                status = url.code
                if status not in range(200,302):
                    print("Site is Down")

        except IOError:
            print("URL error")
            raise SystemExit

        time.sleep(every)



#in seconds
every = 15
url = "https://www.your-url.com"

connect(url, every)
