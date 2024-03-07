from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def check_if_in(object, object_collection):
        if object in object_collection:
            return True
        return False

    def add_customer(self, customer: Customer):
        if not Gym.check_if_in(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if not Gym.check_if_in(trainer, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if not Gym.check_if_in(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if not Gym.check_if_in(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if not Gym.check_if_in(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    @staticmethod
    def from_id(object_id, object_collection):
        return next((o for o in object_collection if o.id == object_id), None)

    def subscription_info(self, subscription_id: int):
        subscription = Gym.from_id(subscription_id, self.subscriptions)
        customer = Gym.from_id(subscription_id, self.customers)
        trainer = Gym.from_id(subscription_id, self.trainers)
        equipment = Gym.from_id(subscription_id, self.equipment)
        plan = Gym.from_id(subscription_id, self.plans)
        result = []

        for x in [subscription, customer, trainer, equipment, plan]:
            result.append(x.__repr__())

        return "\n".join(result)
