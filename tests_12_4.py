import logging
import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='UTF-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_wolk(self):
        try:
            human_test = Runner("Алина", -5)
            if human_test.speed < 0:
                raise ValueError('Скорость не должна быть отрицательной')
            n = 0
            while n != 10:
                human_test.walk()
                n += 1
            self.assertEqual(human_test.distance, 50)
            logging.info(f"test_walk выполнен успешно")
            return human_test.distance
        except ValueError:
            logging.error('Не бывает отрицательной скорости', exc_info=True)
            return 0


    def test_run(self):
        try:
            human_test = Runner("Леха", '1654')
            if isinstance(human_test, int) == False:
                raise ValueError('Неверный тип данных скорости')
            n = 0
            while n != 10:
                human_test.run()
                n += 1
            self.assertEqual(human_test.distance, 100)
            logging.info(f"test_run выполнен успешно")
            return human_test.distance
        except ValueError:
            logging.error('Неверный тип данных скорости', exc_info=True)
            return 0

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
