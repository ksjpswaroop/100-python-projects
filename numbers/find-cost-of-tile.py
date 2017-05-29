def total_cost(w, h, c):
    if w < 0 or h < 0 or c < 0:
        print("Wrong input")
        return -1
    else:
        total = w * h * c
        return total

def msg():
    width = input("Type width: ")
    height = input("Type height: ")
    cost = input("Type cost of tile: ")
    x = total_cost(int(width), int(height), int(cost))
    print ("Total cost of tiles: %s" % x)

msg()
