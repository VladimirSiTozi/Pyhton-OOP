from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return 'barking...'


# Test Code:
b = Dog()
print(b.bark())
print(b.eat())
