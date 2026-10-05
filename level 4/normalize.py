#Normalize an array so its values range from 0 to 1
import numpy as numpy
a = numpy.array([1, 2, 3, 4, 5])
b = (a - numpy.min(a)) / (numpy.max(a) - numpy.min(a))
print(b)