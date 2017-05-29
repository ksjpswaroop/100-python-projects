def mortgage(o, t, i, l):
    if o == "m":
        rate = i / 100 / 12
    elif o == "w":
        rate = i / 100 / 48
    elif o == "d":
        rate = i / 100 / 365
    elif o == "c":
        rate = i / 100
    else:
        print("Wrong input")
        return

    total = (rate / (1 - (1 + rate) ** (-t))) * l
    return total

def msg():
    inpt = input("Select compounding interval (m for Monthly, w for Weekly, d for Daily, c for Continually): ")
    inpt2 = input("Give terms: ")
    inpt3 = input("Give interest: ")
    inpt4 = input("Enter loan value: ")
    result = mortgage(inpt, int(inpt2), float(inpt3), float(inpt4))
    print(result)

msg()
