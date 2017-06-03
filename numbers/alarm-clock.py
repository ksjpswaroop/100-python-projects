from time import strftime,sleep
from os import system

def alarm(h, m, s):
    #hour, minute, second = strftime("%H,%M,%S").split(',') #current time
    seconds = int(h) * 3600 + int(m) * 60 + int(s)
    beep = lambda x: alarm_sound()
    beep(sleep(seconds)) #suspend execution fir the given number of seconds

def alarm_sound():
    system("echo -n '\a';sleep 0.5;" * 30) #30 beeps


def msg():
    inpt_1 = input("Enter Hours: ")
    inpt_2 = input("Enter Minutes: ")
    inpt_3 = input("Enter Seconds: ")
    if (int(inpt_1) >= 0) and (int(inpt_2) in range(0,59)) and (int(inpt_3) in range(0,59)):
        alarm(inpt_1, inpt_2, inpt_3)
    else:
        print("Error")

msg()
