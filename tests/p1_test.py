from convert_nb import convert

import unittest

import numpy as np

convert()
from assignment import problem_1

class TestSolution(unittest.TestCase):
    def test_prob1(self):
        np.testing.assert_string_equal(problem_1(), "Hello, world!")


if __name__ == '__main__':
    unittest.main()