'''
Company Manager
Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. Every one's pay is calculated differently, research a bit about it. After you've established an employee hierarchy, create a Company class that allows you to manage the employees. You should be able to hire, fire and raise employees.
'''
from abc import ABC, abstractmethod


class Company(object):

    def hire_employee(self):
        pass

    def fire_employee(self):
        pass

    def raise_employee(self):
        pass


class Employee(object):

    def __init__(self, name, position, salary, id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = id

    @abstractmethod
    def hours_of_work(self):
        pass

    @abstractmethod
    def overwork(self):
        pass

    def show_employee(self):
        print("Name: {0}\nPosition: {1}\nSalary: {2}\nID: {3}".format(self.name, self.position, self.salary, self.id))
