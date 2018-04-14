'''
Mail Checker (IMAP)
The user enters various account information include
web server and IP, protocol type and the application
will check for email at a given interval.
'''
from imaplib import IMAP4_SSL
import time


def mail_checker(server, username, password, interval):
    try:
        with IMAP4_SSL(server, 993) as M:
            M.login(username, password)
            M.select("INBOX", True)

            while True:
                st, unread = M.search(None, 'UNSEEN')
                total = len(unread[0].split())
                print("You have {0} unseen email/s" .format(total))
                time.sleep(interval)

    except Exception as e:
        print(e)


interval = 15
server = ""
username = ""
password = ""
mail_checker(server, username, password, interval)
