class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
print()

b1 = ImageArea(7, 10)
b2 = ImageArea(35, 2)
b3 = ImageArea(8, 9)
print(b1 != b2)
print(b1 >= b3)
print()

c1 = ImageArea(7, 10)
c2 = ImageArea(35, 2)
c3 = ImageArea(8, 9)
print(c1 <= c2)
print(c1 < c3)