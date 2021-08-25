from assignment import problem_2

import unittest

import numpy as np

class TestSolution(unittest.TestCase):
    def test_prob2(self):
        np.testing.assert_equal(problem_2(2, 4), 6)

if __name__ == '__main__':
    unittest.main()