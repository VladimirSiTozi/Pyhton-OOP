from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return 'Not enough budget'
        if len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_tend = 0
        for animal in self.animals:
            total_tend += animal.money_for_care
        if self.__budget >= total_tend:
            self.__budget -= total_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            else:
                cheetahs.append(animal)

        result.append(f'----- {len(lions)} Lions:')
        for lion in lions:
            result.append(lion.__repr__())

        result.append(f'----- {len(tigers)} Tigers:')
        for tiger in tigers:
            result.append(tiger.__repr__())

        result.append(f'----- {len(cheetahs)} Cheetahs:')
        for cheetah in cheetahs:
            result.append(cheetah.__repr__())

        return '\n'.join(result)

    def workers_status(self):
        result = [f'You have {len(self.workers)} workers']
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
            else:
                vets.append(worker)

        result.append(f'----- {len(keepers)} Keepers:')
        for keeper in keepers:
            result.append(keeper.__repr__())

        result.append(f'----- {len(caretakers)} Caretakers:')
        for caretaker in caretakers:
            result.append(caretaker.__repr__())

        result.append(f'----- {len(vets)} Vets:')
        for vet in vets:
            result.append(vet.__repr__())

        return '\n'.join(result)
