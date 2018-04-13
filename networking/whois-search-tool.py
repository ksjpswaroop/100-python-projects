'''
Whois Search Tool
Enter an IP or host address and have it look it up
through whois and return the results to you.
'''
import socket
from subprocess import call


def whois(ip):
    return call(["whois", ip])


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
    print(whois(given_ip))
