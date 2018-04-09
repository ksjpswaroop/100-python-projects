'''
FTP Program
A file transfer program which can transfer files back and forth from a remote web sever.
'''
from ftplib import FTP

def ftp_upload(choice):

    with FTP('server.address.com','USERNAME','PASSWORD')  as ftp:
        ftp.login()

        file = open('file-name.jpg','rb')
        ftp.storbinary('STOR file-name.jpg', file)
        file.close()


def ftp_download(choice):

    with FTP('server.address.com','USERNAME','PASSWORD') ) as ftp:
        ftp.login()

        file = input("File: ")
        if file not in ftp.nlst():
            print("error File")

        else:
            ftp.retrbinary('RETR ' +file, open(file, 'wb').write)



#console
choice = input("1.Upload\n2.Download\n3.Exit\n---------------\n")

if choice == "1":
    print(ftp_upload(choice))

elif choice == "2":
    print(ftp_download(choice))

elif choice == "3":
    raise SystemExit

else:
    print("error input")
