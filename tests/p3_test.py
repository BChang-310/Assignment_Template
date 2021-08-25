from convert_nb import convert
import unittest

import numpy as np

convert()
from assignment import problem_3

class TestSolution(unittest.TestCase):
    def test_prob3(self):
        np.testing.assert_equal(problem_3(6), 15)

if __name__ == '__main__':
    unittest.main()
