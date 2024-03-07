from project.elf import Elf
from project.hero import Hero
from project.knight import Knight

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
knight = Knight('K', 7)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
print(str(knight))