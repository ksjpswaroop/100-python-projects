
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
restnum = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eigthy','ninety']

def lessthan100(n):
    if n == 0:
        print(numbers[n])
    elif n >= 20 :
        print(tens[int(n/10)])
        print(numbers[int(n%10)])

    elif n in range(10,20):
        print(restnum[int(n%10)])

    else:
        print(numbers[n])


def hundr(n):
    if n >= 100:
        print(str(numbers[int(n/100)]) + ' hundred')
        lessthan100(int(n%100))
    else:
        lessthan100(n)

def spell(n):
    if n >= 1000:
        print(str(numbers[int(n/1000)]) + ' thousand')
        hundr(int(n%1000))
    elif n >= 100:
        hundr(n)
    else:
        lessthan100(n)


def msg():
    num = input("Type a number: ")
    spell(int(num))

msg()
