#Find duplicate values in a NumPy array.
import numpy as numpy
arr=numpy.array([1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 10])
unique, counts = numpy.unique(arr, return_counts=True)
duplicates = unique[counts > 1]
print("Duplicate values in the array:", duplicates)