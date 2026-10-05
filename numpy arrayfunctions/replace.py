# Replace all negative values with 0.
import numpy as numpy
array = numpy.array([-1, 2, -3, 4, -5])
result = numpy.where(array < 0, 0, array)
print(result)