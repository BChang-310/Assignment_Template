from assignment import problem_3

import unittest

import numpy as np

class TestSolution(unittest.TestCase):
    def test_prob3(self):
        np.testing.assert_equal(problem_3(6), 15)

if __name__ == '__main__':
    unittest.main()