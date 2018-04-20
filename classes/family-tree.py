class Person(object):

    def __init__(self, fname, lname, born=None, died=None):
        self.fname = fname
        self.lname = lname
        self.born = born
        self.died = died
        self.siblings_list = None

    def parents(self, mother=None, father=None):
        self.mother = mother
        self.father = father

    def siblings(self, *args):
        self.siblings_list = []
        for arg in args:
            self.siblings_list.append(arg)

    def grandparents(self, granddad=None, grandmother=None):
        self.granddad = granddad
        self.grandmother = grandmother


    def get_members(self):
        family_members = {"First name": self.fname,
                          "Last name" : self.lname,
                          "Grandfather": self.granddad,
                          "Grandmother": self.grandmother,
                          "Father": self.father,
                          "Mother": self.mother,
                          "Siblings": self.siblings_list
                         }

        return family_members


class Relations(object):

    def __init__(self):
        self.child = {}
        self.partners = {}

    def get_child(self, person):

        #for grandfathers and grandmothers childs
        #supposedly the child got its father's last name
        if person["Last name"] in person["Father"]:
            self.child[person["Grandfather"]] = person["Father"]
            self.child[person["Grandmother"]] = person["Father"]

        elif person["Last name"] in person["Mother"]:
            self.child[person["Grandfather"]] = person["Mother"]
            self.child[person["Grandmother"]] = person["Mother"]

        #for parents childs
        self.child[person["Mother"]] = person["Siblings"]
        self.child[person["Father"]] = person["Siblings"]
        return self.child


    def get_partners(self, person):
        self.partners[person["Grandfather"]] = person["Grandmother"]
        self.partners[person["Father"]] = person["Mother"]

        return self.partners
