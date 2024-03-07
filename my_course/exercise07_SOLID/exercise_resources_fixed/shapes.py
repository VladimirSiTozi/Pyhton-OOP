from abc import ABC, abstractmethod
from cmath import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        a = 1/2 * self.width * self.height
        return a


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        a = self.width * self.height
        return a


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def calculate_area(self):
        a = pi * self.radius ** 2
        return a


class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("`shapes` should be of type `list`.")
        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(4)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
