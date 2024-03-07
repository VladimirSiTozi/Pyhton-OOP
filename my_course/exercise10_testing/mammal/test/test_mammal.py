from unittest import TestCase, main

from OOP.exercise10_testing.mammal.project.mammal import Mammal
# from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('Mani', 'Mammoth', 'mammoth_sound')

    def test_correct_init(self):
        self.assertEqual("Mani", self.mammal.name)
        self.assertEqual('Mammoth', self.mammal.type)
        self.assertEqual('mammoth_sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_should_return_the_sound_of_the_mammal(self):
        expected_result = self.mammal.make_sound()
        self.assertEqual(f"Mani makes mammoth_sound", expected_result)

    def test_get_kingdom_should_return_the_animal_kingdom(self):
        expected_result = self.mammal.get_kingdom()
        self.assertEqual('animals', expected_result)

    def test_info_should_return_the_animal_is_of_what_type(self):
        expected_result = self.mammal.info()
        self.assertEqual("Mani is of type Mammoth", expected_result)

if __name__ == '__main__':
    main()