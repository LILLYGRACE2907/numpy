# Count multiples of 5 in a NumPy array.
import numpy as numpy
array = numpy.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
result = numpy.sum(array % 5 == 0)
print(result)