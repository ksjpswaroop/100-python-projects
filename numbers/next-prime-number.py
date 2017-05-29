import math
def is_prime():
    x = [2]
    for value in range(3,1000):
        if value % 2 == 0 and value > 2:
            continue
        if all(value % i for i in range(3, int(math.sqrt(value)) + 1, 2)):
            x.append(value)
    return x


def msg():
    x = is_prime()
    for value in range(len(x)):
        inpt = input("Show more prime numbers? Y/N: ")
        if inpt == 'N' or inpt == 'n':
            return 0
        elif inpt == 'Y' or inpt == 'y':
            print (x[value])

msg()
