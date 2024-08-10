import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runners = [
            Runner(name='Усейн', speed=10),
            Runner(name='Андрей', speed=9),
            Runner(name='Ник', speed=3)
        ]

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_tournament_trios(self):
        self.all_results.append(Tournament(90, *self.runners).start())
        self.all_results.append(Tournament(90, self.runners[1], self.runners[2], self.runners[0]).start())
        self.all_results.append(Tournament(90, self.runners[2], self.runners[0], self.runners[1]).start())

    def test_tournament_couples_01(self):
        result = Tournament(90, self.runners[0], self.runners[1]).start()
        self.all_results.append(result)
        self.assertEqual({1: self.runners[0], 2: self.runners[1]}, result)

        result = Tournament(90, self.runners[1], self.runners[0]).start()
        self.all_results.append(result)
        self.assertEqual({1: self.runners[0], 2: self.runners[1]}, result)

    def test_tournament_couples_02(self):
        result = Tournament(90, self.runners[0], self.runners[2]).start()
        self.all_results.append(result)
        self.assertEqual({1: self.runners[0], 2: self.runners[2]}, result)

        result = Tournament(90, self.runners[2], self.runners[0]).start()
        self.all_results.append(result)
        self.assertEqual({1: self.runners[0], 2: self.runners[2]}, result)

    def test_tournament_couples_12(self):
        result = Tournament(90, self.runners[1], self.runners[2]).start()
        self.all_results.append(result)
        self.assertEqual({1: self.runners[1], 2: self.runners[2]}, result)

        result = Tournament(90, self.runners[2], self.runners[1]).start()
        self.all_results.append(result)
        self.assertEqual({1: self.runners[1], 2: self.runners[2]}, result)


if __name__ == '__main__':
    unittest.main()
