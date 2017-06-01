def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error division"

def mult(x,y):
    return x * y


def msg():
    inpt_1 = input("Add sign: ")
    inpt_2 = input("Add first number: ")
    inpt_3 = input("Add second number: ")
    if inpt_1 == "+":
        print(add(float(inpt_2),float(inpt_3)))
    elif inpt_1 == "-":
        print(subtract(float(inpt_2),float(inpt_3)))
    elif inpt_1 == "/":
        print(division(float(inpt_2),float(inpt_3)))
    elif inpt_1 == "*":
        print(mult(float(inpt_2),float(inpt_3)))
    else:
        print("Error")



msg()
