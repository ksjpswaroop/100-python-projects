'''
Flower Shop Ordering To Go
Create a flower shop application which deals in flower objects and use those flower objects in a bouquet object which can then be sold. Keep track of the number of objects and when you may need to order more.
'''

class FlowerShop(object):

    def __init__(self):
        self.flowers = {}
        self.min_flowers = 2

    def add_flower(self, ftype, number):
        if ftype not in self.flowers.keys():
            self.flowers[ftype] = number
        else:
            self.flowers[ftype] += number

    def show_flowers(self):
        print(self.flowers)

    def bouquet(self, flower, number):
        if flower in self.flowers.keys():
            if number <= self.flowers[flower]:
                self.flowers[flower] -= number
                if self.flowers[flower] < 2:
                    self.add_flower(flower, self.min_flowers)
            else:
                print("not enough flowers")


########
shop = FlowerShop()

shop.add_flower("Rose", 1)
shop.add_flower("Rose", 1)
shop.add_flower("Rose", 1)
shop.add_flower("Rose", 1)
shop.add_flower("Lily", 1)
shop.add_flower("Lily", 1)
shop.add_flower("Lily", 1)

shop.show_flowers()
shop.bouquet("Rose", 3)
shop.show_flowers()
