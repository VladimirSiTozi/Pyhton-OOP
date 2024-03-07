
from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ['Vegetables', 'Fruits']
    WEIGHT_GAINED = 0.15

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_GAINED = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ['Meat', 'Vegetables']
    WEIGHT_GAINED = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_GAINED = 1

    def make_sound(self):
        return "ROAR!!!"

