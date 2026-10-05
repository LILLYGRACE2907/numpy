#Solve a system of linear equations using np.linalg.solve().
import numpy as numpy
a = numpy.array([[3, 1], [1, 2]])
b = numpy.array([9, 8])
x = numpy.linalg.solve(a, b)
print(x)