#Stack two arrays vertically using vstack().
import numpy as numpy
a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[5, 6]])
c = numpy.vstack((a, b))
print(c)