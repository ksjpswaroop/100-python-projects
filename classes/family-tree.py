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
        father = person["Father"].split()[1]
        mother = person["Mother"].split()[1]
        if father in person["Grandfather"]:
            self.child[person["Grandfather"]] = person["Father"]
            self.child[person["Grandmother"]] = person["Father"]

        elif mother in person["Grandfather"]:
            self.child[person["Grandfather"]] = person["Mother"]
            self.child[person["Grandmother"]] = person["Mother"]

        #for person's childs
        self.child[person["First name"] + " " + person["Last name"]] = person["Siblings"]

        #parents childs
        self.child[person["Mother"]] = person["First name"] + " " + person["Last name"]
        self.child[person["Father"]] = person["First name"] + " " + person["Last name"]

        return self.child


    def get_partners(self, person):
        self.partners[person["Grandfather"]] = person["Grandmother"]
        self.partners[person["Grandmother"]] = person["Grandfather"]
        self.partners[person["Father"]] = person["Mother"]
        self.partners[person["Mother"]] = person["Father"]

        return self.partners
