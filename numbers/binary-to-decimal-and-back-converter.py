import math
def convertion(dec, bi):
    binary = []
    while int(dec) >= 1:
        if int(dec) % 2 == 0:
            binary.append(0)
        elif int(dec) % 2 == 1:
            binary.append(1)
        dec = dec / 2
    binary = binary[::-1]
    print(binary)

    decimal = []
    bi = list(map(int, str(bi)))
    bi = bi[::-1]
    for num in range(len(bi)):
        decimal.append(bi[num] * math.pow(2,num))
    print(sum(decimal))




def msg():
    inpt_1 = input("Give decimal number: ")
    inpt_2 = input("Give binary number: ")
    convertion(int(inpt_1),int(inpt_2))

msg()
