class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius: int):
        self.radius = new_radius

    def get_area(self):
        A = self.pi * self.radius ** 2
        return A

    def get_circumference(self):
        C = self.pi * (self.radius * 2)
        return C

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())



