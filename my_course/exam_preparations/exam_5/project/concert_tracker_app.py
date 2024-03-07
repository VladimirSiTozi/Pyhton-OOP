from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        musician = self.is_musician_exist(name)
        if musician:
            raise Exception(f"{musician.name} is already a musician!")
        current_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(current_musician)
        return f"{current_musician.name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self.is_band_exist(name)
        if band:
            raise Exception(f"{band.name} band is already created!")
        current_band = Band(name)
        self.bands.append(current_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.is_concert_exist(place)
        if concert:
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")
        current_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(current_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.is_musician_exist(musician_name)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        band = self.is_band_exist(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.is_band_exist(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        musician = next((m for m in band.members if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = next((c for c in self.concerts if c.place == concert_place), None)
        band = next((b for b in self.bands if b.name == band_name), None)
        all_members_have_needed_skills = False

        if len(band.members) == 0:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            drummer = next((d for d in band.members if 'play the drums with drumsticks' in d.skills), None)
            singer = next((s for s in band.members if 'sing high pitch notes' in s.skills), None)
            guitarist = next((g for g in band.members if 'play rock' in g.skills), None)
            if drummer and singer and guitarist:
                all_members_have_needed_skills = True

        elif concert.genre == "Metal":
            drummer = next((d for d in band.members if 'play the drums with drumsticks' in d.skills), None)
            singer = next((s for s in band.members if 'sing low pitch notes' in s.skills), None)
            guitarist = next((g for g in band.members if 'play metal' in g.skills), None)
            if drummer and singer and guitarist:
                all_members_have_needed_skills = True

        elif concert.genre == "Jazz":
            drummer = next((d for d in band.members if 'play the drums with drum brushes' in d.skills), None)
            singer = next((s for s in band.members if ('sing high pitch notes' and 'sing low pitch notes') in s.skills),
                          None)
            guitarist = next((g for g in band.members if 'play jazz' in g.skills), None)
            if drummer and singer and guitarist:
                all_members_have_needed_skills = True

        if all_members_have_needed_skills:
            profit = (concert.audience * concert.ticket_price) - concert.expenses
            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

        raise Exception(f"The {band_name} band is not ready to play at the concert!")

    def is_musician_exist(self, name):
        musician_is_exist = next((m for m in self.musicians if m.name == name), None)
        return musician_is_exist

    def is_concert_exist(self, place):
        is_concert_exist = next((c for c in self.concerts if c.place == place), None)
        return is_concert_exist

    def is_band_exist(self, name):
        is_band_exist = next((b for b in self.bands if b.name == name), None)
        return is_band_exist
