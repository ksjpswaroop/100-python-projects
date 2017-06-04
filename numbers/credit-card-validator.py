
def luhn(x):   #luhn algorithm for credit card validation
    j = 1
    d = []
    for i in x:
        if j % 2 == 0:
            d.append(int(i))
        else:
            dual = int(i) * 2
            if dual >= 10:
                f = str(dual)
                a = f[0]
                b = f[1]
                d.append(int(a) + int(b))
            else:
                d.append(dual)
        j+=1
    if sum(d) % 10 == 0:
        print("Valid")
    else:
        print("Not valid")



def msg():
    inpt = input("Credit card number: ")
    luhn(inpt)



msg()
