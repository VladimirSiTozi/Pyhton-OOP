from unittest import TestCase, main

from OOP.exercise10_testing.hero.project.hero import Hero
# from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Pesho', 25, 100.0, 40.0)

    def test_correct_init(self):
        self.assertEqual('Pesho', self.hero.username)
        self.assertEqual(25, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(40.0, self.hero.damage)

    def test_correct_init_values(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_battle_hero_cannot_fight_with_himself_raises_error(self):
        enemy_hero = Hero('Pesho', 25, 100.0, 40.0)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_lower_than_one_raises_error(self):
        self.hero.health = 0
        enemy_hero = Hero('Ivan', 25, 100.0, 40.0)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual(f"Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual(f"Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_hero_health_lower_than_one_raises_error111(self):
        enemy_hero = Hero('Ivan', 25, -10.0, 40.0)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ve.exception))

        enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_battle_draw_result_both_heroes_health_dropped_below_one(self):
        self.hero.damage = 150
        enemy_hero = Hero('Ivan', 25, 100.0, 150)

        expected_result = 'Draw'
        actual_result = self.hero.battle(enemy_hero)

        self.assertEqual(expected_result, actual_result)

    def test_battle_hero_win(self):
        enemy_hero = Hero('Ivan', 1, 1, 1)

        expected_result = 'You win'
        actual_result = self.hero.battle(enemy_hero)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(25 + 1, self.hero.level)
        self.assertEqual(99 + 5, self.hero.health)
        self.assertEqual(40 + 5, self.hero.damage)

    def test_battle_hero_lose(self):
        self.hero.health = 10
        self.hero.damage = 10
        enemy_hero = Hero('Ivan', 190, 600, 350)

        expected_result = 'You lose'
        actual_result = self.hero.battle(enemy_hero)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(190 + 1, enemy_hero.level)
        self.assertEqual(350 + 5, enemy_hero.health)
        self.assertEqual(350 + 5, enemy_hero.damage)

    def test_str_method(self):
        actual_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(actual_result, str(self.hero))


if __name__ == '__main__':
    main()