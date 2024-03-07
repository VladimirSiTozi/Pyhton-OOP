from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in Tournament.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        current_equipment = Tournament.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(current_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in Tournament.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."
        current_team = Tournament.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(current_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        current_equipment = next((e for e in self.equipment[::-1] if e.__class__.__name__ == equipment_type), None)
        current_team = next((t for t in self.teams if t.name == team_name), None)

        if current_equipment.price > current_team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(current_equipment)
        current_team.equipment.append(current_equipment)
        current_team.budget -= current_equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        current_team = next((t for t in self.teams if t.name == team_name), None)
        if current_team is None:
            raise Exception("No such team!")
        if current_team.wins > 0:
            raise Exception(f"The team has {current_team.wins} wins! Removal is impossible!")

        self.teams.remove(current_team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                number_of_changed_equipment += 1
        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_name1 = next((t for t in self.teams if t.name == team_name1), None)
        team_name2 = next((t for t in self.teams if t.name == team_name2), None)

        if team_name1.__class__.__name__ != team_name2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_name1_total_protection = sum(e.protection for e in team_name1.equipment)
        team_name1_total_point = team_name1.advantage + team_name1_total_protection

        team_name2_total_protection = sum(e.protection for e in team_name2.equipment)
        team_name2_total_point = team_name2.advantage + team_name2_total_protection

        if team_name1_total_point == team_name2_total_point:
            return "No winner in this game."

        elif team_name1_total_point > team_name2_total_point:
            team_name1.win()
            return f"The winner is {team_name1.name}."

        else:
            team_name2.win()
            return f"The winner is {team_name2.name}."

    def get_statistics(self):
        result = [f'Tournament: {self.name}',
                  f'Number of Teams: {len(self.teams)}',
                  'Teams:']

        sorted_team = sorted(self.teams, key=lambda x: -x.wins)

        for team in sorted_team:
            result.append(team.get_statistics())

        return "\n".join(result)