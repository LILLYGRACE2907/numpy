#Stack two arrays horizontally using hstack().
import numpy as numpy
a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[5, 6]])
c = numpy.hstack((a, b))
print(c)