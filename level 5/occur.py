# Find values that occur exactly once.
import numpy as numpy 
arr=numpy.array([1, 2, 3, 4, 5, 1, 2, 3])
unique, counts = numpy.unique(arr, return_counts=True)
once = unique[counts == 1]
print("Values that occur exactly once:", once)