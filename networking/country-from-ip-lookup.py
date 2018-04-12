'''
Country from IP Lookup
Enter an IP address and find the country that IP is registered in.
Optional: Find the Ip automatically.
'''
import socket
import urllib.request
import json


def country(ip):
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    URL = "https://geoip-db.com/jsonp/" + ip
    with urllib.request.urlopen(urllib.request.Request(URL, None, headers)) as url:
        page = url.read()
        jsonp = page[len('callback('):-1]
        data = json.loads(jsonp.decode())
        print(data['country_name'])


def valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True

    except socket.error:
        print("Not a valid ip.")
        raise SystemExit


#console
given_ip = input("IP: ")

if valid_ip(given_ip):
    country(given_ip)
