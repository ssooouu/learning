import unittest
import test
import test_2

run_test = unittest.TestSuite()
turn_test = unittest.TestSuite()

run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test.RunnerTest))
turn_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_2.TournamentTest))

runner_1 = unittest.TextTestRunner(verbosity=2)
runner_1.run(run_test)

tournament_1 = unittest.TextTestRunner(verbosity=2)
tournament_1.run(turn_test)
