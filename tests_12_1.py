import unittest
from unittest import TestCase

from runner import Runner


class RunnerTest(TestCase):
    def test_wolk(self):
        human_test = Runner("Алина")
        n = 0
        while n != 10:
            human_test.walk()
            n += 1
        self.assertEqual(human_test.distance, 50)

    def test_run(self):
        human_test = Runner("Леха")
        n = 0
        while n != 10:
            human_test.run()
            n += 1
        self.assertEqual(human_test.distance, 100)

    def test_challenge(self):
        human_test_2 = Runner("Леха")
        n = 0
        while n != 10:
            human_test_2.run()
            n += 1
        self.assertEqual(human_test_2.distance, 100)

        human_test_1 = Runner("Алина")
        n = 0
        while n != 10:
            human_test_1.walk()
            n += 1
        self.assertEqual(human_test_1.distance, 50)

        self.assertNotEqual(human_test_2.distance, human_test_1)

if __name__ == '__main__':
    unittest.main()
