from unittest import TestCase, main

from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList(
            '50',
            1,
            False,
            3.5,
            2,
            3
        )

    def test_correct_initialization(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_operation_adds_integer_to_the_list(self):
        expected_data = self.integer_list.get_data() + [49]

        actual_data = self.integer_list.add(49)

        self.assertEqual(expected_data, actual_data)

    def test_add_operation_raises_error_due_to_not_integer_given_to_add_operation(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_operation_with_out_of_range_index_should_raise_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(99)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index__with_valid_index_should_remove_element_from_the_list(self):
        expected_data = [2, 3]
        deleted_element = 1

        actual_deleted_element = self.integer_list.remove_index(0)

        self.assertEqual(expected_data, self.integer_list.get_data())
        self.assertEqual(deleted_element, actual_deleted_element)

    def test_get_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(99)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index_return_element(self):
        expected_element = 2
        actual_element = self.integer_list.get(1)

        self.assertEqual(expected_element, actual_element)

    def test_insert_integer_with_valid_expect_insert_element(self):
        extended_list = [1, 2, 4, 3]

        self.integer_list.insert(2, 4)

        self.assertEqual(extended_list, self.integer_list.get_data())

    def test_insert_with_invalid_index_expect_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(99, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_not_integer_element_expect_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(0, 'psst')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest_should_return_the_biggest_integer_in_the_list(self):
        expected_result = 3
        actual_result = self.integer_list.get_biggest()

        self.assertEqual(expected_result, actual_result)

    def test_get_index_should_return_the_index_fn_the_given_element(self):
        expected_result = 0
        actual_result = self.integer_list.get_index(1)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
