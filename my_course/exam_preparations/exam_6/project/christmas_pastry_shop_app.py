from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if next((d for d in self.delicacies if d.name == name), None):
            raise Exception(f"{name} already exists!")

        current_delicacy = ChristmasPastryShopApp.VALID_DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(current_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in ChristmasPastryShopApp.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        if next((b for b in self.booths if b.booth_number == booth_number), None):
            raise Exception(f"Booth number {booth_number} already exists!")

        current_booth = ChristmasPastryShopApp.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(current_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)

        if booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)

        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        # self.delicacies.remove(delicacy) ## not mentioned
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)

        price_of_all_orders = sum(p.price for p in booth.delicacy_orders)
        bill = booth.price_for_reservation + price_of_all_orders

        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."



