import unittest

from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def test_Tournament_1(self):
        run = Tournament(90, self.runner_1, self.runner_3)
        a = run.start()
        TournamentTest.all_result = a
        a = max(a)
        flag = False
        if TournamentTest.all_result[a] == 'Ник':
            flag = True
            self.assertTrue(flag)
        print(TournamentTest.all_result)


        run2 = Tournament(90, self.runner_2, self.runner_3)
        a_2 = run2.start()
        TournamentTest.all_result = a_2
        a_2 = max(a_2)
        flag = False
        if TournamentTest.all_result[a_2] == 'Ник':
            flag = True
            self.assertTrue(flag)
        print(TournamentTest.all_result)

        run3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        a_3 = run3.start()
        TournamentTest.all_result = a_3
        a_3 = max(a_3)
        flag = False
        if TournamentTest.all_result[a_3] == 'Ник':
            flag = True
            self.assertTrue(flag)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_result)


if __name__ == '__main__':
    unittest.main()
