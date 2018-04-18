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


class Manager(object):

    def __init__(self):
        self.recipe_list = {}
        self.deserts = {}
        self.main_courses = {}

    def add_recipe(self, name, recipe, type):
        self.recipe_list[name] = recipe

        if type == "Main course":
            self.main_courses[name] = recipe

        elif type == "Desert":
            self.deserts[name] = recipe

    def show_recipes(self):
        for k, l in self.recipe_list.items():
            print(k + ": " + str(l))

    def show_deserts(self):
        for k, l in self.deserts.items():
            print(k + ": " + str(l))

    def show_main_courses(self):
        for k, l in self.main_courses.items():
            print(k + ": " + str(l))
