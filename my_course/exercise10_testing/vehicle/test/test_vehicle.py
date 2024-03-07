from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(50.5, 98.5)

    def test_correct_init(self):
        self.assertEqual(50.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(98.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_attribute_types(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))

    def test_drive_distance_is_reachable_decrease_car_fuel(self):
        expected_result = 50.5 - 1.25
        self.vehicle.drive(1)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_drive_distance_is_unreachable_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_fuel_is_not_too_much_and_increase_the_car_fuel(self):
        expected_result = 10 + 3
        self.vehicle.fuel = 10

        self.vehicle.refuel(3)

        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_fuel_is_too_much_and_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        expected_result = "The vehicle has 98.5 horse power with 50.5 fuel left and 1.25 fuel consumption"
        actual_result = self.vehicle.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()