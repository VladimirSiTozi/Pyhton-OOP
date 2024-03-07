from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEAL_TYPES = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        if next((c for c in self.clients_list if client_phone_number == client_phone_number), None):
            raise Exception("The client has already been registered!")

        current_client = Client(client_phone_number)
        self.clients_list.append(current_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEAL_TYPES.keys():
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = [m.details() for m in self.menu]

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try:
            self.register_client(client_phone_number)
        except Exception:
            pass

        current_client = next(c for c in self.clients_list)

        for meal, quantity in meal_names_and_quantities.items():
            menu_meal = next((m for m in self.menu if m.name == meal), None)
            current_meal = self.VALID_MEAL_TYPES[meal](meal, quantity)

            if menu_meal is None:
                raise Exception(f"{meal} is not on the menu!")

            if menu_meal.quantity > current_meal.quantity:
                raise Exception(f"Not enough quantity of {current_meal.__class__.__name__}: {current_meal.name}!")

            menu_meal.quantity -= quantity
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * quantity

        meal_names = [m.name for m in current_client.shopping_cart]

        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        current_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")
        current_client.shopping_cart.clear()
        current_client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        current_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        current_bill = current_client.bill

        current_client.shopping_cart.clear()
        current_client.bill = 0

        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {current_bill:.2f} was successfully paid " \
               f"for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
