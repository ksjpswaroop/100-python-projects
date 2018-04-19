'''
Recipe Creator and Manager
Create a recipe class with ingredients and a put them in a recipe manager program that organizes them into categories like deserts, main courses or by ingredients like chicken, beef, soups, pies etc.
'''
from collections import defaultdict


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
        self.ingredients = defaultdict(list)

    def add_recipe(self, name, recipe, type):
        self.recipe_list[name] = recipe

        if type == "Main course":
            self.main_courses[name] = recipe

        elif type == "Desert":
            self.deserts[name] = recipe

    def show_all_ingredients(self):
        for k, lista in self.recipe_list.items():
            for l in lista:
                self.ingredients[l].append(k)

        for k, l in self.ingredients.items():
            print(k + ": " + str(l))

    def show_all_recipes(self):
        for k, l in self.recipe_list.items():
            print(k + ": " + str(l))

    def show_deserts(self):
        for k, l in self.deserts.items():
            print(k + ": " + str(l))

    def show_main_courses(self):
        for k, l in self.main_courses.items():
            print(k + ": " + str(l))

    def show_recipe(self, rec_name):
        if rec_name in self.recipe_list.keys():
            print(self.recipe_list[rec_name])
        else:
            print("error recipe")


#############################
rec1 = Recipe("potato","carrot","salt").get_ingredients()
rec2 = Recipe("rice","salt","chicken").get_ingredients()
rec3 = Recipe("beans","chilli","sausage","salt").get_ingredients()
rec4 = Recipe("sugar","strawberry","milk").get_ingredients()
rec5 = Recipe("milk","sugar","flour").get_ingredients()
rec6 = Recipe("potato","steak","salt","pepper","onions").get_ingredients()

manager = Manager()

manager.add_recipe("Recipe 1", rec1, "Main course")
manager.add_recipe("Recipe 2", rec2, "Main course")
manager.add_recipe("Recipe 3", rec3, "Main course")
manager.add_recipe("Recipe 4", rec4, "Desert")
manager.add_recipe("Recipe 5", rec5, "Desert")
manager.add_recipe("Recipe 6", rec6, "Main course")

#manager.show_all_recipes()
#manager.show_main_courses()
#manager.show_deserts()
#manager.show_all_ingredients()
#manager.show_recipe("Recipe 6")
