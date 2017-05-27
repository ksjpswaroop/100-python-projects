from mpmath import mp

def printmsg():
    number = input('Type a number: ')
    return picalc(number)

def picalc(number):
    if number > 10**4:
        print("Big number, try again...")
        return printmsg()
    else:
         mp.dps = number
         print(mp.euler)
printmsg()
