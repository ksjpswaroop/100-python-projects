import math
def sieve(n):
    x = [2]
    for value in range(3,n):
        if value % 2 == 0 and value > 2:
            continue
        if all(value % i for i in range(3, int(math.sqrt(value)) + 1, 2)):
            x.append(value)
    return x


print(sieve(10000))
