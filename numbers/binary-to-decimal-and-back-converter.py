import math
import re

def dectobi(dec):
    binary = []
    while int(dec) >= 1:
        if int(dec) % 2 == 0:
            binary.append(0)
        elif int(dec) % 2 == 1:
            binary.append(1)
        dec = dec / 2
    binary = binary[::-1]
    print(binary)

def bitodec(bi):
    decimal = []
    bi = list(map(int, str(bi)))
    bi = bi[::-1]
    for num in range(len(bi)):
        decimal.append(bi[num] * math.pow(2,num))
    print(sum(decimal))



def bincheck(inpt_2):
    is_bin = re.compile(r"[01]+").match
    if bool(is_bin(inpt_2)):
        bitodec(int(inpt_2))
    else:
        print("Not a binary")


def msg():
    inpt_1 = input("Give decimal number: ")
    inpt_2 = input("Give binary number: ")
    dectobi(int(inpt_1))
    bincheck(inpt_2)

msg()
