import matplotlib.pyplot
from matplotlib.pyplot import show
import numpy as np
from matplotlib.pyplot import bar
dataset = {"c": 40, "java": 45, "python": 50}
courses = dataset.values()
values = dataset.keys()
bar(values , courses,color="blue")
matplotlib.pyplot.xlabel("Courses offered")
matplotlib.pyplot.ylabel("No. of students enrolled")
matplotlib.pyplot.title("Students enrolled in different courses")
matplotlib.pyplot.show()
