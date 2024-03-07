from unittest import TestCase, main

from cat import Cat


class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Ivan')

    def test_correct_initialization(self):
        self.cat = Cat('Ivan')
        self.assertEqual('Ivan', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_cat_should_feed_true_sleepy_true_and_size_plus_one(self):
        # arrange
        expected_size = 1

        # act
        self.cat.eat()

        # assert
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_eat_cat_is_already_feed_should_raise_error(self):
        # arrange
        self.cat.fed = True

        # act
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        # assert
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_cat_is_not_feed_makes_cat_not_sleepy(self):
        # arrange
        self.cat.fed = True
        self.cat.sleepy = True

        # act
        self.cat.sleep()

        # arrange
        self.assertFalse(self.cat.sleepy)

    def test_sleeping_when_cat_is_hungry_and_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
