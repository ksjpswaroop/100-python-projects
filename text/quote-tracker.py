'''
Quote Tracker (crypto symbols etc)
A program which can go out and check the current value of cryptocurrencies for a list of symbols entered by the user.
The user can set how often the cryptocurrencies are checked. For CLI, show whether the cryptocurrency has moved up or down.
'''

import urllib.request
import json
import time

def cryptoprices(sym):
    #coinmarketcap api link, works for 100 cryptocurrencies (add limit for more)
    ticker = "https://api.coinmarketcap.com/v1/ticker/"
    prices = {}

    headers = { 'User-Agent' : 'Mozilla/5.0' }
    page = urllib.request.Request(ticker, None, headers)
    page = urllib.request.urlopen(page)
    data = page.read()
    encoding = page.info().get_content_charset('utf-8')
    data = json.loads(data.decode(encoding))
    page.close()

    for x in data:
        for i in range(0,len(sym)):
            if x['symbol']==sym[i]:
                prices[sym[i]] = x['price_usd']
                sym.remove(sym[i])
                break

    print(prices)
    if sym:
        print('Not found: ' + str(sym))


seconds_interval = 10

while True:
    inpt = ['BTC','LTC']
    cryptoprices(inpt)
    time.sleep(seconds_interval)
