import unittest

import RunnerTest
import TournamentTest

suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest),
    unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest)
])

unittest.TextTestRunner(verbosity=2).run(suite)



