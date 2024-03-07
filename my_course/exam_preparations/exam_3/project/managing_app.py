from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        system_user = next((su for su in self.users if su.driving_license_number == driving_license_number), None)
        if system_user is None:
            current_user = User(first_name, last_name, driving_license_number)
            self.users.append(current_user)
            return f"{current_user.first_name} {current_user.last_name} was successfully registered under " \
                   f"DLN-{driving_license_number}"
        return f"{driving_license_number} has already been registered to our platform."

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        system_plate_number = next((p for p in self.vehicles if p.license_plate_number == license_plate_number), None)
        if system_plate_number:
            return f"{license_plate_number} belongs to another vehicle."

        current_vehicle = ManagingApp.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(current_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        system_route_check = next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point), None)
        if system_route_check:
            if system_route_check.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif system_route_check.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            else:
                system_route_check.is_locked = True

        current_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(current_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        current_user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        current_vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        current_route = next((r for r in self.routes if r.route_id == route_id), None)

        if current_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if current_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if current_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        current_vehicle.drive(current_route.length)

        if is_accident_happened:
            current_vehicle.is_damaged = True
            current_user.decrease_rating()
        else:
            current_user.increase_rating()

        return current_vehicle.__str__()

    def repair_vehicles(self, count: int):
        count_of_repaired_vehicles = 0
        sorted_vehicles = sorted(self.vehicles, key=lambda car: (car.brand, car.model))
        for vehicle in sorted_vehicles:
            if vehicle.is_damaged and count_of_repaired_vehicles < count:
                vehicle.is_damaged = False
                vehicle.recharge()
                count_of_repaired_vehicles += 1
        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        result = ['*** E-Drive-Rent ***']
        sorted_user_list = sorted(self.users, key=lambda x: -x.rating)
        for user in sorted_user_list:
            result.append(user.__str__())
        return '\n'.join(result)


