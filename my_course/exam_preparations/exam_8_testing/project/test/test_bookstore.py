from project.bookstore import Bookstore

from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(100)

    def test_correct_initialization(self):
        self.assertEqual(100, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_book_limit_setter_if_limit_is_equal_or_below_zero_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        expected_result = "Books limit of 0 is not valid"

        self.assertEqual(expected_result, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -10

        expected_result = "Books limit of -10 is not valid"

        self.assertEqual(expected_result, str(ve.exception))

    def test_len_method_should_return_book_count(self):
        self.bookstore.availability_in_store_by_book_titles.update({'Mobi Dick': 2})
        self.bookstore.availability_in_store_by_book_titles.update({'Hobbit': 1})

        actual_result = self.bookstore.__len__()
        expected_result = 3

        self.assertEqual(expected_result, actual_result)

    def test_receive_book_unsuccessfully_not_enough_space_in_the_bookstore_raises_error(self):
        self.bookstore.books_limit = 1
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Kerry', 3)

        expected_result = "Books limit is reached. Cannot receive more books!"

        self.assertEqual(expected_result, str(ex.exception))

    def test_receive_book_successfully_is_enough_space_returns_the_number_of_copies(self):
        actual_result = self.bookstore.receive_book('Kerry', 3)

        expected_result = "3 copies of Kerry are available in the bookstore."

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {'Kerry': 3})

    def test_sell_book_unsuccessfully_if_book_is_not_available_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Kerry', 1)

        expected_result = "Book Kerry doesn't exist!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})

    def test_sell_book_unsuccessfully_if_book_exist_but_not_enough_copies_raises_error(self):
        self.bookstore.receive_book('Kerry', 1)

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Kerry', 3)

        expected_result = "Kerry has not enough copies to sell. Left: 1"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {'Kerry': 1})

    def test_sell_book_successfully(self):
        self.bookstore.receive_book('Kerry', 3)

        actual_result = self.bookstore.sell_book('Kerry', 1)

        expected_result = 'Sold 1 copies of Kerry'
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {'Kerry': 2})
        self.assertEqual(self.bookstore.total_sold_books, 1)

    def test_str_method(self):
        self.bookstore.receive_book('Kerry', 3)

        self.bookstore.sell_book('Kerry', 1)

        expected_result = 'Total sold books: 1\n' \
                          'Current availability: 2\n' \
                          ' - Kerry: 2 copies'

        actual_result = self.bookstore.__str__()

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()
