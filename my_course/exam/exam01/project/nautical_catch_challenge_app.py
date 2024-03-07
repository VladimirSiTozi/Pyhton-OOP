from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if self.is_diver_registered(diver_name):
            return f"{diver_name} is already a participant."

        current_diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(current_diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self.is_fish_registered(fish_name):
            return f"{fish_name} is already permitted."

        current_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(current_fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        current_diver = self.is_diver_registered(diver_name)
        current_fish = self.is_fish_registered(fish_name)

        if current_diver is None:
            return f"{diver_name} is not registered for the competition."

        if current_fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if current_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if current_diver.oxygen_level < current_fish.time_to_catch:
            current_diver.miss(current_fish.time_to_catch)

            if current_diver.oxygen_level == 0:
                current_diver.has_health_issue = True

            return f"{diver_name} missed a good {fish_name}."

        elif current_diver.oxygen_level == current_fish.time_to_catch:
            if is_lucky:
                current_diver.hit(current_fish)

                if current_diver.oxygen_level == 0:
                    current_diver.has_health_issue = True

                return f"{diver_name} hits a {current_fish.points}pt. {fish_name}."

            current_diver.miss(current_fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        else:
            current_diver.hit(current_fish)

            if current_diver.oxygen_level == 0:
                current_diver.has_health_issue = True

            return f"{diver_name} hits a {current_fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_recovered = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                divers_recovered += 1

        return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        current_diver = self.is_diver_registered(diver_name)

        result = [f'**{diver_name} Catch Report**']

        fishes_caught = [f.fish_details() for f in current_diver.catch]
        for fish in fishes_caught:
            result.append(fish)

        return '\n'.join(result)

    def competition_statistics(self):
        result = ['**Nautical Catch Challenge Statistics**']
        sorted_divers = sorted(self.divers, key=lambda x: (-x.competition_points, len(x.catch), x.name))

        for diver in sorted_divers:
            if diver.has_health_issue is False:
                result.append(diver.__str__())

        return '\n'.join(result)

    def is_diver_registered(self, diver_name):
        return next((d for d in self.divers if d.name == diver_name), None)

    def is_fish_registered(self, fish_name):
        return next((f for f in self.fish_list if f.name == fish_name), None)
