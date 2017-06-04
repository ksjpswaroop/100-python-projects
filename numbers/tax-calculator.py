
def calculator(c, t):
    rate = t / 100
    tax = rate * c
    total = tax + c
    print('Tax: '+ str(tax))
    print('Cost: '+ str(total))


def msg():
    cost = input("Enter Cost \n")
    tax = input("Enter Tax (in %) \n")
    calculator(float(cost), float(tax))



msg()
