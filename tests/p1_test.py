from assignment import problem_1

import unittest

import numpy as np

class TestSolution(unittest.TestCase):
    def test_prob1(self):
        np.testing.assert_string_equal(problem_1(), "Hello, world!")


if __name__ == '__main__':
    unittest.main()