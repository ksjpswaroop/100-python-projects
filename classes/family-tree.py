'''
Family Tree Creator
Create a class called Person which will have a name, when they were born and when (and if) they died. Allow the user to create these Person classes and put them into a family tree structure. Print out the tree to the screen.
'''

class Person(object):

    def __init__(self, fname, lname, born, died=None):
        self.fname = fname
        self.lname = lname
        self.born = born
        self.died = died
        self.mother = ""
        self.father = ""
        self.grandmother = ""
        self.granddad = ""
        self.siblings_list = []

    def parents(self, mother, father):
        self.mother = mother
        self.father = father

    def siblings(self, *args):
        for arg in args:
            self.siblings_list.append(arg)

    def grandparents(self, granddad, grandmother):
        self.granddad = granddad
        self.grandmother = grandmother

    def show_members(self):
        print(self.fname + " " + self.lname, self.mother, self.father, self.grandmother, self.granddad, self.siblings_list)
