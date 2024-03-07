from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.is_horse_already_exist(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_TYPES:
            current_horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(current_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.is_jockey_already_exist(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        current_jockey = Jockey(jockey_name, age)
        self.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.is_horse_race_already_exist(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        current_horse_race = HorseRace(race_type)
        self.horse_races.append(current_horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        current_jockey = self.is_jockey_already_exist(jockey_name)
        current_horse = next((h for h in self.horses[::-1] if (h.__class__.__name__ == horse_type and not h.is_taken)),
                             None)

        if current_jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if current_horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if current_horse and current_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        current_horse.is_taken = True
        current_jockey.horse = current_horse

        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        current_jockey = self.is_jockey_already_exist(jockey_name)
        current_race = self.is_horse_race_already_exist(race_type)

        if current_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if current_jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if current_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for race in self.horse_races:
            if next((j for j in race.jockeys if j.name == jockey_name), None):
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        current_race = self.is_horse_race_already_exist(race_type)

        if current_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None

        for jockey in current_race.jockeys:
            if winner is None:
                winner = jockey
                continue

            if winner.horse.speed < jockey.horse.speed:
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."



    def is_horse_already_exist(self, horse_name):
        horse = next((h for h in self.horses if h.name == horse_name), None)
        return horse

    def is_jockey_already_exist(self, jockey_name):
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        return jockey

    def is_horse_race_already_exist(self, race_type):
        horse_race = next((r for r in self.horse_races if r.race_type == race_type), None)
        return horse_race
