#. Split an array into three equal parts.
import numpy as numpy
a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = numpy.split(a, 3)
c=numpy.array_split(a, 3)
print(b)
print(c)