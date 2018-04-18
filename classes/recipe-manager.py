'''
Recipe Creator and Manager
Create a recipe class with ingredients and a put them in a recipe manager program that organizes them into categories like deserts, main courses or by ingredients like chicken, beef, soups, pies etc.
'''

class Recipe(object):

    def __init__(self, *args):
        self.ingredients = []
        for arg in args:
            self.ingredients.append(arg)

    def get_ingredients(self):
        return self.ingredients
