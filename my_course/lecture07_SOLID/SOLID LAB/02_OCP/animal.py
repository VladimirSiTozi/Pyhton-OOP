from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        for animal in animals:
            print(animal.make_sound())


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Cat(Animal):
    def make_sound(self):
        return 'meow-meow'

    
class Frog(Animal):
    def make_sound(self):
        return 'croak'


class Tiger(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        return f'{self.name} is ROARing!'


class Chicken(Animal):
    def make_sound(self):
        return 'chicken sound'


animals = [Cat('cat'), Dog('dog'), Frog('frog'), Tiger('tiger'), Chicken('Chiko')]


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animal_sound(animals)
