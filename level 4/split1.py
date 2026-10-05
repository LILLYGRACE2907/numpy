 #Split a 2D matrix into two vertical sections.
import numpy as numpy
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.vsplit(a, 2)
c = numpy.array_split(a, 2, axis=1)
print(b)