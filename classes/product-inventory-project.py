'''
Product Inventory Project
Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.
'''
import itertools


class Product:
    newid = itertools.count()
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.id = next(Product.newid)
        self.quantity = quantity

    def update_name(self, new_name):
        self.name = new_name

    def update_price(self, new_price):

        if new_price > 0:
            self.price = new_price
        else:
            print("price error")

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("quantity error")

    def print_product(self):
        print("ID: {0}\nName: {1}\nPrice: {2}\nQuantity: {3}" .format(self.id, self.name, self.price, self.quantity))
