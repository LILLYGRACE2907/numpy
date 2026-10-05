#Calculate the Euclidean norm of a vector.
import numpy as numpy
a = numpy.array([1, 2, 3])
b = numpy.linalg.norm(a)
c = numpy.linalg.norm(a, ord=1)
print(b)
print(c)