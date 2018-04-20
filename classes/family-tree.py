'''
Family Tree Creator
Create a class called Person which will have a name, when they were born and when (and if) they died. Allow the user to create these Person classes and put them into a family tree structure. Print out the tree to the screen.
'''

class Person(object):

    def __init__(self, name, born=None, died=None):
        self.name = name
        self.born = born
        self.died = died
        self.relations = {}

    def add_relation(self, type, person):
        if type not in self.relations.keys():
            self.relations[type] = []
        self.relations[type].append(person)

    def get_relation(self, type):
        try:
            if type is None:
                pass
            else:
                return self.relations[type][0].name
        except:
            pass

    def get_relations(self, type):
        try:
            return self.relations[type]
        except:
            return None

    def add_parents(self, mother, father):
        mother.add_child(self)
        father.add_child(self)

    def add_child(self, child):
        self.add_relation("children", child)
        child.add_relation("parents", self)

    def add_spouse(self, spouse):
        self.add_relation("spouse", spouse)
        spouse.add_relation("spouse", self)

    def get_parents(self):
        return self.get_relations("parents")

    def get_children(self):
        return self.get_relations("children")

    def get_spouse(self):
        return self.get_relation("spouse")


def tree(person):
    parents = [person.name]

    if person.get_spouse() is not None:
        parents.append(person.get_spouse())

    if len(parents) == 1:
        print(parents[0])
    else:
        print(parents[0], parents[1])

    try:
        for child in person.get_children():
            #print('-----{}'.format(child))
            tree(child)
    except:
        pass
