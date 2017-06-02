def temprtr(x):
    f = -17.2222222
    c =  38.8
    ch = input("Select:\n 1.F to C \n 2.C to F \n")
    temp = input("Number: ")
    if ch == "1":
        print(float(temp) / f)

    elif ch == "2":
        print(float(temp) / c)

    else:
        print("Wrong input")



def curnc(inpt_1):
    ch = input("Select:\n 1.E to $ \n 2.$ to E \n")
    cur = input("Number: ")
    e = 1.127315
    d = 0.887063509
    if ch == "1":
        print(float(cur) * d)

    elif ch == "2":
        print(float(cur) * e)

    else:
        print("Wrong input")


def volum(x):
    ch = input("Select:\n 1.Galon to Litre \n 2.Litre to Galon \n")
    vol = input("Number: ")
    l = 0.264172052
    g = 3.78541178
    if ch == "1":
        print(float(vol) * g)
    elif ch == "2":
        print(float(vol) * l)
    else:
        print("Wrong input")




def mss(x):
    ch = input("Select:\n 1.Kilos to Pounds \n 2.Pounds to Kilos \n")
    mass = input("Number: ")
    k = 2.204622621849
    p = 0.45359237
    if ch == "1":
        print(float(mass) * k)

    elif ch == "2":
        print(float(mass) * p)


    else:
        print("Wrong input")


def msg():
    inpt_1 = input("Press:\n 1.Temp \n 2.Currency \n 3.Volume \n 4.Mass \n")
    if inpt_1 == "1":
        temprtr(inpt_1)
    elif inpt_1 == "2":
        curnc(inpt_1)
    elif inpt_1 == "3":
        volum(inpt_1)
    elif inpt_1 == "4":
        mss(inpt_1)
    else:
        print("Wrong input")



msg()
