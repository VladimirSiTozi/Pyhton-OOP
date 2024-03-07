from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.t1f = Trip(10000, 1, False)
        self.t2f = Trip(10000, 2, False)
        self.t2t = Trip(10000, 2, True)

    def test_correct_initialization(self):
        self.assertEqual(10000, self.t1f.budget)
        self.assertEqual(1, self.t1f.travelers)
        self.assertEqual(False, self.t1f.is_family)
        self.assertEqual({}, self.t1f.booked_destinations_paid_amounts)

        self.assertEqual(10000, self.t1f.budget)
        self.assertEqual(1, self.t1f.travelers)
        self.assertEqual(False, self.t1f.is_family)
        self.assertEqual({}, self.t1f.booked_destinations_paid_amounts)

    def test_setter_travellers_if_less_than_one_return_error(self):
        with self.assertRaises(ValueError) as ve:
            self.t1f.travelers = -10

        self.assertEqual('At least one traveler is required!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.t1f.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_setter_is_family_if_less_than_two_return_false(self):
        self.assertTrue(self.t2t.is_family)

        self.t1f.is_family = Trip
        self.assertFalse(self.t1f.is_family)

    def test_book_a_trip_not_in_offers(self):
        actual_result = self.t2t.book_a_trip('something else')
        self.assertEqual(actual_result, 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_not_enough_budget(self):
        actual_result = self.t2t.book_a_trip("New Zealand")
        self.assertEqual(actual_result, 'Your budget is not enough!')

    def test_book_a_trip_successfully_without_discount(self):
        actual_result = self.t2f.book_a_trip('Bulgaria')
        expected_result = 'Successfully booked destination Bulgaria! Your budget left is 9000.00'
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(9000, self.t2f.budget)
        self.assertEqual({'Bulgaria': 1000},self.t2f.booked_destinations_paid_amounts)

    def test_book_a_trip_successfully_with_discount(self):
        actual_result = self.t2t.book_a_trip('Bulgaria')
        expected_result = 'Successfully booked destination Bulgaria! Your budget left is 9100.00'
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(9100, self.t2t.budget)
        self.assertEqual({'Bulgaria': 900}, self.t2t.booked_destinations_paid_amounts)

    def test_booking_status_empty_destinations(self):
        actual_result = self.t1f.booking_status()
        expected_result = 'No bookings yet. Budget: 10000.00'

        self.assertEqual(actual_result, expected_result)

    def test_booking_status_successfully_with_any_destination(self):
        self.t2f.budget = 100_000
        self.t2f.book_a_trip('Brazil')
        self.t2f.book_a_trip('New Zealand')

        expected_result = '''Booked Destination: Brazil
Paid Amount: 12400.00
Booked Destination: New Zealand
Paid Amount: 15000.00
Number of Travelers: 2
Budget Left: 72600.00'''

        actual_result = self.t2f.booking_status()

        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    main()