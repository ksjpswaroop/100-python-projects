x = [1,1]
inpt = input('Type a number: ')
for i in xrange(inpt):
    x.append(x[-1] + x[-2])
    print(x[i])
