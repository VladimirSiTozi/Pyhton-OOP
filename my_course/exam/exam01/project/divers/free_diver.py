from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=120)

    def miss(self, time_to_catch: int):
        points_to_reduce = time_to_catch * 0.6

        if self.oxygen_level - round(points_to_reduce) < 0:
            self.oxygen_level = 0
            return

        self.oxygen_level -= round(points_to_reduce)

    def renew_oxy(self):
        self.oxygen_level = 120
