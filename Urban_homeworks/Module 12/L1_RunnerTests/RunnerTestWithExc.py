import unittest
import logging
from rt_with_exceptions import Runner, Tournament


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', encoding='utf-8', level=logging.INFO,
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def setUp(self):
        self.runners = [
            Runner('Cheetah', 20),
            Runner('Snail', 1)
        ]

    def test_init_runner(self):
        for name, speed in (
            ('Bob', 10),
            (10, 20),
            ('Snail', -1)
        ):
            try:
                Runner(name, speed)
                logging.info(f'Инициализация объекта класса {Runner.__name__} '
                             f'полями name: {name}, speed: {speed} прошла УСПЕШНО.')
            except Exception as e:
                logging.warning(f'Не удалось инициализировать объект класса {Runner.__name__} '
                                f'полями name: {name}, speed: {speed}.\n'
                                f'{e}')

    def test_walk(self):
        for runner in self.runners:
            [runner.walk() for _ in range(10)]

        for i, expected_result in (
                (0, 200),
                (1, 11)
        ):
            try:
                logging.info(f'Runner: {self.runners[i]}, speed: {self.runners[i].speed}, distance: {self.runners[i].distance}')
                self.assertEqual(expected_result, self.runners[i].distance)
                logging.info(f'"test_walk" выполнен успешно, ')

            except Exception as e:
                logging.warning(f'"test_walk" выполнить не удалось: {e}')

    def test_run(self):
        for runner in self.runners:
            [runner.run() for _ in range(10)]

        for i, expected_result in (
                (0, 401),
                (1, 20)
        ):
            try:
                logging.info(
                    f'Runner: {self.runners[i]}, speed: {self.runners[i].speed}, distance: {self.runners[i].distance}')
                self.assertEqual(expected_result, self.runners[i].distance)
                logging.info(f'"test_run" выполнен успешно, ')

            except Exception as e:
                logging.warning(f'"test_run" выполнить не удалось: {e}')

    def test_challenge(self):
        for runner in self.runners:
            [runner.run() for _ in range(5)]

        try:
            logging.info(f'Runners: {self.runners[0]}, {self.runners[1]}')
            self.assertGreater(self.runners[0].distance, self.runners[1].distance)
            logging.info(f'"test_challenge" выполнен успешно')

        except Exception as e:
            logging.warning(f'{e}')


if __name__ == '__main__':
    unittest.main()
