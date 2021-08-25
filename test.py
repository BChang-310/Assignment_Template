import unittest

from unittest.mock import MagicMock

import nbconvert
import numpy as np

with open("assignment.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

with open("assignment.py", "w") as f:
    f.write(python_file)

from assignment import AnotherClass

class TestSolution(unittest.TestCase):

    def test_AnotherClass(self):
        thisisit = AnotherClass()
        np.testing.assert_array_almost_equal(thisisit.MyFunc(1),1,decimal=6)

    def test_AnotherClassAgain(self):
        thisisit = AnotherClass()
        np.testing.assert_array_almost_equal(thisisit.MyFunc(2),2,decimal=6)


if __name__ == '__main__':
    unittest.main()
