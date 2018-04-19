'''
Shape Area and Perimeter Classes
Create an abstract class called Shape and then inherit from it other shapes like diamond, rectangle, circle, triangle etc. Then have each class override the area and perimeter functionality to handle each shape type.
'''
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*self.width + 2*self.height


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side


class Triangle(Shape):

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        S = self.perimeter()/2
        return math.sqrt(S*(S - self.side_a)*(S - self.side_b)*(S - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return 2*math.pi*self.radius
