#. Calculate the determinant of a 2×2 matrix using np.linalg.det().
import numpy as numpy
a = numpy.array([[1, 2], [3, 4]])
determinant = numpy.linalg.det(a)
print(determinant)