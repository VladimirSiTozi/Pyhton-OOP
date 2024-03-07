from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch: int):
        points_to_reduce = time_to_catch * 0.3

        if self.oxygen_level - round(points_to_reduce) < 0:
            self.oxygen_level = 0
            return

        self.oxygen_level -= round(points_to_reduce)

    def renew_oxy(self):
        self.oxygen_level = 540
