def prime_factor(n):
    prime_list = []
    value = 2
    while value * value <= n:
        if n % value:
            value = value + 1
        else:
            n = n // value
            prime_list.append(value)
    if n > 1:
        prime_list.append(n)
    return prime_list

def msg():
    inpt = raw_input("Type a number: ")
    x = prime_factor(int(inpt))
    print x

msg()
