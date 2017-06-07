import random

def flippin(n):
    heads = []
    tails = []
    for num in range(0,n):
        x = random.randrange(0, 101, 2)
        if x < 50:
            heads.append('Heads')
        else:
            tails.append('Tails')
    return 'Heads: ' + str(len(heads))+ '\nTails: ' + str(len(tails))

def msg():
    times = input("Give number of coin flips: ")
    print(flippin(int(times)))

msg()
