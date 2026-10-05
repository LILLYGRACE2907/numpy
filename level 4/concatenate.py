#71. Concatenate two NumPy arrays using concatenate().
import numpy as numpy
a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[5, 6]])
c = numpy.concatenate((a, b), axis=0)
print(c)