class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = int(health)

    def defend(self, damage: int):
        self.health -= int(damage)
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount: int):
        self.health += int(amount)


hero = Hero("Peter", 100)

print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

