from unittest import TestCase, main

from car_manager import Car


class TestCarManger(TestCase):
    def setUp(self) -> None:
        self.car_manger = Car('Toyota', 'Supra', 12, 90)

    def test_correct_initialization(self):
        self.assertEqual('Toyota', self.car_manger.make)
        self.assertEqual('Supra', self.car_manger.model)
        self.assertEqual(12, self.car_manger.fuel_consumption)
        self.assertEqual(90, self.car_manger.fuel_capacity)
        self.assertEqual(0, self.car_manger.fuel_amount)

    def test_no_make_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car('', 'Supra', 12, 90)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Toyota', '', 12, 90)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_negative_or_zero_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Toyota', 'Supra', -1, 90)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_negative_or_zero_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Toyota', 'Supra', 12, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.car_manger.fuel_amount -= 5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_negative_or_zero_amount_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.car_manger.refuel(-5)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_more_fuel_than_capacity_fills_to_capacity(self):
        self.car_manger.refuel(120)
        expected_result = 90

        self.assertEqual(expected_result, self.car_manger.fuel_amount)

    def test_drive_car_with_valid_fuel(self):
        self.car_manger.refuel(100)
        self.car_manger.drive(10)

        self.assertEqual(90 - 1.2, self.car_manger.fuel_amount)

    def test_drive_car_with_invalid_fuel(self):
        self.car_manger.refuel(100)
        with self.assertRaises(Exception) as ex:
            self.car_manger.drive(20000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
