from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot,  "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in RobotsManagingApp.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")
        current_service = RobotsManagingApp.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(current_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in RobotsManagingApp.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        current_robot = RobotsManagingApp.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(current_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next((r for r in self.robots if r.name == robot_name), None)
        service = next((s for s in self.services if s.name == service_name), None)

        if not (robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'SecondaryService') or \
                (robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'SecondaryService'):
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise "Not enough capacity for this robot!"

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_service = next((s for s in self.services if s.name == service_name), None)
        current_robot = next((r for r in current_service.robots if r.name == robot_name), None)

        if current_robot is None:
            raise Exception("No such robot in this service!")
        current_service.robots.remove(current_robot)
        self.robots.append(current_robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        number_of_robots_fed = 0
        current_service = next((s for s in self.services if s.name == service_name), None)

        for robot in current_service.robots:
            robot.eating()
            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        current_service = next((s for s in self.services if s.name == service_name), None)
        total_price = sum([robot.price for robot in current_service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return '\n'.join(result)





