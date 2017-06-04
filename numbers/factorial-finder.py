
def finder_loops(n):
    factorial = 1
    for digit in range(1,int(n)):
        factorial = digit * factorial + factorial
    print("Factorial: "+ str(factorial))


def finder_rec(n,x):
    x = n * x
    return finder_rec(n-1,x) if n > 1 else print('Factorial: ' + str(x))


def msg():
    inpt = input("Give positive integer \n")
    finder_loops(inpt)
    x = 1
    if inpt == '0':
        print('Factorial: 1')
    else:
        finder_rec(int(inpt),x)

msg()
