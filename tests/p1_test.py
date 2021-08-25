import unittest
import nbconvert
import numpy as np
import os

print(os.getcwd())

with open("./assignment.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

with open("assignment.py", "w") as f:
    f.write(python_file)

from assignment import problem_1

class TestSolution(unittest.TestCase):
    def test_prob1(self):
        np.testing.assert_string_equal(problem_1(), "Hello, world!")


if __name__ == '__main__':
    unittest.main()
