from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @Horse.speed.setter
    def speed(self, value):
        if value > self.MAXIMUM_SPEED:
            raise ValueError("Horse speed is too high!")
        self._Horse__speed = value

    def train(self):
        if self.speed + 2 > self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED
            return
        self.speed += 2
