from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.railway_station = RailwayStation('Vidin Railway Station')

    def test_correct_initialization(self):
        self.assertEqual('Vidin Railway Station', self.railway_station.name)
        self.assertEqual(deque([]), self.railway_station.arrival_trains)
        self.assertEqual(deque([]), self.railway_station.departure_trains)

    def test_name_setter_if_len_of_name_is_less_than_4_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = 'epa'

        expected_result = 'Name should be more than 3 symbols!'

        self.assertEqual(expected_result, str(ve.exception))

    def test_new_arrival_on_board(self):
        self.railway_station.new_arrival_on_board('T1')
        self.assertEqual(self.railway_station.arrival_trains, deque(['T1']))

        self.railway_station.new_arrival_on_board('T2')
        self.assertEqual(self.railway_station.arrival_trains, deque(['T1', 'T2']))

    def test_train_has_arrived_unsuccessfully_trains_did_not_matches(self):
        self.railway_station.new_arrival_on_board('T1')

        actual_result = self.railway_station.train_has_arrived('T2')
        expected_result = 'There are other trains to arrive before T2.'

        self.assertEqual(actual_result, expected_result)

    def test_train_has_arrived_successfully_train_pop_from_arrivals(self):
        self.railway_station.new_arrival_on_board('T1')

        actual_result = self.railway_station.train_has_arrived('T1')
        expected_result = "T1 is on the platform and will leave in 5 minutes."

        self.assertEqual(actual_result, expected_result)

    def test_train_has_left_unsuccessfully_trains_did_not_matches(self):
        self.railway_station.departure_trains.append('T1')
        self.railway_station.departure_trains.append('T2')

        actual_result = self.railway_station.train_has_left('T2')
        expected_result = False

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.railway_station.departure_trains, deque(['T1', 'T2']))

    def test_train_has_left_successfully_trains_matches(self):
        self.railway_station.departure_trains.append('T1')
        self.railway_station.departure_trains.append('T2')

        actual_result = self.railway_station.train_has_left('T1')
        expected_result = True

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.railway_station.departure_trains, deque(['T2']))


if __name__ == '__main__':
    main()
