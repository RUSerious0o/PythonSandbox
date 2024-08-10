import unittest
# from pprint import pprint

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            Runner(name='Усейн', speed=10),
            Runner(name='Андрей', speed=9),
            Runner(name='Ник', speed=3)
        ]

    # def tearDownClass(cls):
    #     pprint(cls.all_results)

    def tournamentTest(self):
        print(Tournament(90, self.runners[0], self.runners[1]).start())
        self.assertEqual(0, 1)

    def someTest(self):
        self.assertEqual(Runner('Abc', 5).distance, 0)


if __name__ == '__main__':
    unittest.main()
