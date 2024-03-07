from project.truck_driver import TruckDriver

from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.truck_driver = TruckDriver('Ivan', 10)

    def test_correct_initialization(self):
        self.assertEqual('Ivan', self.truck_driver.name)
        self.assertEqual(10, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_less_than_zero_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -10

        self.assertEqual(f"Ivan went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_successfully(self):
        actual_result = self.truck_driver.add_cargo_offer('Sofia', 100)
        expected_result = "Cargo for 100 to Sofia was added as an offer."

        self.assertEqual(actual_result, expected_result)

    def test_add_cargo_offer_unsuccessfully_cargo_already_added_raises_error(self):
        self.truck_driver.available_cargos['Sofia'] = 100

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer('Sofia', 100)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer_successfully(self):
        self.truck_driver.available_cargos['Sofia'] = 100
        self.truck_driver.available_cargos['Vidin'] = 150

        actual_result = self.truck_driver.drive_best_cargo_offer()
        expected_result = "Ivan is driving 150 to Vidin."

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.truck_driver.earned_money, 150 * 10)
        self.assertEqual(self.truck_driver.miles, 150)
        #  self.assertEqual(self.truck_driver.check_for_activities(150), 150)

    def test_drive_best_cargo_offer_unsuccessfully_no_available_offers_raises_error(self):
        actual_result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", actual_result)

    def test_check_for_activities(self):
        self.truck_driver.check_for_activities(100)


if __name__ == '__main__':
    main()