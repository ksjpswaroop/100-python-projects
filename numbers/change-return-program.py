from math import floor

def change_return(cost, money):
    change = money - cost
    if change < 0:
        print("Need more money")
        exit
    elif change == 0:
        print("No change")
    else:
        print("Your change is %f" % change)
        change = change * 100
        quarters = floor(change/100)
        print("%d quarters." % quarters)
        change = change - quarters*100
        dimes = floor(change/25)
        print("%d dimes." % dimes)
        change = change - dimes * 25
        nickels = floor(change/10)
        print("%d nickels." % nickels)
        change = change - nickels * 10
        pennies = floor(change/1)
        print("%d pennies." % pennies)

def msg():
    inpt_1 = input("Cost?  ")
    inpt_2 = input("Money given?  ")
    change_return(float(inpt_1),float(inpt_2))

msg()
