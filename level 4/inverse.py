#Calculate the inverse of a matrix using np.linalg.inv().
import numpy as numpy
a = numpy.array([[1, 2], [3, 4]])
inverse = numpy.linalg.inv(a)
print(inverse)