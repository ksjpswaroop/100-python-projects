import math

x = []
def distance(n0,n1):
    x.append([n0,n1])
    return math.sqrt((n0[0] - n1[0])**2 + (n0[1] - n1[1])**2)

def closest(points):
    i = 0
    mylist = []
    for i in range(i,len(points)):
        j = i+1
        for j in range(j,len(points)):
            mylist.append(distance(points[i],points[j]))
    test = mylist.index(min(mylist))
    print("Points: " + str(x[test]))
    return min(mylist)

points = [[13,81],[28,67],[56,99],[64,31],[73,82],[28,21],[44,92]]
print("Distance: " + str(closest(points)))
