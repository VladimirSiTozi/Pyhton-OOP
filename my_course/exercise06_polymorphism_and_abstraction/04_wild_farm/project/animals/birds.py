from abc import ABC, abstractmethod
from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_GAINED = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOODS = ['Meat', 'Vegetables', 'Fruits', 'Seed']
    WEIGHT_GAINED = 0.35

    def make_sound(self):
        return "Cluck"
