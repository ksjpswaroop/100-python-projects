def square(x):
    return x**2

def happy(n):
    x = []
    for digit in n:
        x.append(int(digit))
    number = sum(map(square,x))
    if number == 1:
        print("HAPPY")
    elif number == 4:
        print("NOT HAPPY")
    else:
        return happy(str(number))



def msg():
    num = input("Type a number: ")
    happy(num)

msg()
