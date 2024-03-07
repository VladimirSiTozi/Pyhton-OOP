from project.toy_store import ToyStore


from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_correct_initialization(self):
        expected_result = {"A": None,
                           "B": None,
                           "C": None,
                           "D": None,
                           "E": None,
                           "F": None,
                           "G": None,
                           }
        actual_result = self.toy_store.toy_shelf

        self.assertEqual(actual_result, expected_result)

    def test_add_toy_unsuccessfully_shelf_does_not_exist_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('V', 'Woody the cowboy')

        expected_result = "Shelf doesn't exist!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_add_toy_unsuccessfully_toy_is_already_in_that_shelf_raises_error(self):
        self.toy_store.toy_shelf['A'] = 'Woody the cowboy'

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Woody the cowboy')

        expected_result = "Toy is already in shelf!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_add_toy_unsuccessfully_shelf_is_already_taken_by_another_toy_raises_error(self):
        self.toy_store.toy_shelf['A'] = 'Woody the cowboy'

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Buzz Lightyear')

        expected_result = "Shelf is already taken!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_add_toy_successfully(self):
        actual_result = self.toy_store.add_toy('A', 'Buzz Lightyear')
        expected_result = "Toy:Buzz Lightyear placed successfully!"

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.toy_store.toy_shelf['A'], 'Buzz Lightyear')

    def test_remove_toy_unsuccessfully_shelf_does_not_exist_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('V', 'Woody the cowboy')

        expected_result = "Shelf doesn't exist!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_remove_toy_unsuccessfully_there_is_another_toy_on_that_shelf_raises_error(self):
        self.toy_store.toy_shelf['A'] = 'Woody the cowboy'

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'Buzz Lightyear')

        expected_result = "Toy in that shelf doesn't exists!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_remove_toy_successfully(self):
        self.toy_store.toy_shelf['A'] = 'Woody the cowboy'

        actual_result = self.toy_store.remove_toy('A', 'Woody the cowboy')
        expected_result = "Remove toy:Woody the cowboy successfully!"

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.toy_store.toy_shelf['A'], None)


if __name__ == '__main__':
    main()
