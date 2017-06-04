
def addition(x,y):
    print((x[0]+y[0])+(x[1]+y[1]))

def negation(x,y):
    print((x[0]+y[0])-(x[1]+y[1]))

def multiplication(x,y):
    print((x[0]+x[1])*(y[0]+y[1]))

def inversion(x):
    print(1/(x[0]+x[1]))



num_1 = [4,3j]
num_2 = [3,7j]
addition(num_1,num_2)
negation(num_1,num_2)
multiplication(num_1,num_2)
inversion(num_1)
