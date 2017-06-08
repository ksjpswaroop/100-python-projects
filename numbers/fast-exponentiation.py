def pow_fast(res,a,b):
    if b == 1:
        print(res)
    else:
        res = res * a
        b-=1
        return pow_fast(res,a,b)


def msg():
    inpt_1 = input("Enter a: ")
    inpt_2 = input("Enter b: ")
    pow_fast(int(inpt_1),int(inpt_1),int(inpt_2))



msg()
