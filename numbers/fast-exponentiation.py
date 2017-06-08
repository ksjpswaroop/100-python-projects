def pow_fast(a,b):
    if b == 0:
      return 1
    else:
        if(b % 2 == 0):
            res = pow_fast(a, b / 2)
            return res * res
        else:
            res = pow_fast(a, (b-1) / 2)
            return res * res * a



def msg():
    inpt_1 = input("Enter a: ")
    inpt_2 = input("Enter b: ")
    print(pow_fast(int(inpt_1),int(inpt_2)))



msg()
