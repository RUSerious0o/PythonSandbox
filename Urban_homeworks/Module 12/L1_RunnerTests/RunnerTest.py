import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Bob')
        [runner.walk() for _ in range(10)]
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('George')
        [runner.run() for _ in range(10)]
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runners = [
            Runner('Slowpoke'),
            Runner('Cheetah')
        ]
        for _ in range(10):
            runners[0].walk()
            runners[1].run()
        self.assertNotEqual(runners[0], runners[1])


if __name__ == '__main__':
    unittest.main()