from unittest import TestCase, main

from worker import Worker


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker('TestGuy', 25000, 100)

    def test_correct_initialization(self):
        #  arrange, act, assert
        self.worker = Worker('TestGuy', 25000, 100)
        self.assertEqual('TestGuy', self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_energy_money_increase_and_energy_decrease(self):
        # arrange
        expected_energy = self.worker.energy - 1
        expected_money = self.worker.salary

        # act
        self.worker.work()

        # assert
        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_when_worker_try_to_work_but_energy_is_zero_and_raise_error(self):
        self.worker.energy = 0  # arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()  # act

        self.assertEqual('Not enough energy.', str(ex.exception))  # assert

    def test_rest_when_worker_rest_energy_increases(self):
        expected_energy = self.worker.energy + 1  # assert

        self.worker.rest()  # act

        self.assertEqual(self.worker.energy, expected_energy)  # assert

    def test_get_info_return_valid_string(self):
        self.assertEqual(
            self.worker.get_info(), f'{self.worker.name} has saved {self.worker.money} money.')


if __name__ == '__main__':
    main()