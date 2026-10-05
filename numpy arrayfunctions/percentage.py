#Calculate the percentage contribution of each value to the total.
import numpy as numpy
array = numpy.array([1, 2, 3, 4, 5])
total = numpy.sum(array)
percentages = (array / total) * 100
print(percentages)