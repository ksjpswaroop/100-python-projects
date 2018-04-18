'''
Company Manager
Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. Every one's pay is calculated differently, research a bit about it. After you've established an employee hierarchy, create a Company class that allows you to manage the employees. You should be able to hire, fire and raise employees.
'''
from abc import ABC, abstractmethod


class Company(object):

    def __init__(self):
        self.employees = {"HourlyEmployee": 93,
                          "SalariedEmployee": 31,
                          "Manager": 8,
                          "Executive": 1}

    def hire_employee(self, id, position):
        if position in self.employees.keys():
            self.employees[position] += 1

    def fire_employee(self, id, position):
        if position in self.employees.keys():
            self.employees[position] -= 1

    def raise_employee(self, id, position, raise_m):
        if position in self.employees.keys():
            name = "John"
            salary = 2900
            employee = Employee(name, position, salary+int(raise_m), id)
            employee.show_employee()


class Employee(object):

    def __init__(self, name, position, salary, id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = id

    @abstractmethod
    def salary(self):
        pass

    def show_employee(self):
        print("Name: {0}\nPosition: {1}\nSalary: {2}\nID: {3}".format(self.name, self.position, self.salary, self.id))


class HourlyEmployee(Employee):

    def __init__(self, id, work_hours, age):
        self.id = id
        self.work_hours = work_hours
        self.age = age

    def salary(self):

        if self.age > 26:
            total_salary = (self.work_hours*200) + 200
            return total_salary
        else:
            total_salary = self.work_hours*200
            return total_salary


class SalariedEmployee(Employee):

    def __init__(self, id, overwork_hours, age):
        self.id = id
        self.overwork_hours = overwork_hours
        self.age = age

    def salary(self):

        if self.age > 26:
            total_salary = (8*200) + 200 + (self.overwork_hours*300)
            return total_salary

        else:
            total_salary = (8*200) + (self.overwork_hours*300)
            return total_salary


class Manager(Employee):

    def __init__(self, id, overwork_hours, age):
        self.id = id
        self.overwork_hours = overwork_hours
        self.age = age

    def salary(self):
        if self.age > 26:
            total_salary = (8*200) + 200 + (self.overwork_hours*300) + 500
            return total_salary

        else:
            total_salary = (8*200) + 500 + (self.overwork_hours*300)
            return total_salary


class Executive(Employee):

    def __init__(self, id, overwork_hours, age):
        self.id = id
        self.overwork_hours = overwork_hours
        self.age = age

    def salary(self):
        if self.age > 26:
            total_salary = (8*200) + 200 + (self.overwork_hours*300) + 1500
            return total_salary

        else:
            total_salary = (8*200) + 1500 + (self.overwork_hours*300)
            return total_salary


#some tests
employee = Employee("John", "Manager", 2900, 2)
employee.show_employee()
hourlyemployee = HourlyEmployee(1,6,27)
print("Hourly employee: {}".format(hourlyemployee.salary()))

salariedemployee = SalariedEmployee(1,2,27)
print("Salaried employee: {} " .format(salariedemployee.salary()))

manager = Manager(1,2,27)
print("Manager: {}".format(manager.salary()))

executive = Executive(1,2,27)
print("Executive: {}".format(executive.salary()))


company= Company()
print(company.employees)
company.hire_employee(1,"HourlyEmployee")
print(company.employees)
company.fire_employee(2,"SalariedEmployee")
print(company.employees)

company.raise_employee(2,"Manager",200)
