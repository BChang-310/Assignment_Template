import nbconvert
import glob

assignment_nb = glob.glob('../*.ipynb')[0]

with open(assignment_nb) as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

with open("assignment.py", "w") as f:
    f.write(python_file)
