#replace all values greater than 100 with 100
import numpy as numpy
array = numpy.array([50, 150, 200, 75, 25])
result = numpy.where(array > 100, 100, array)
print(result)