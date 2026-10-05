# Find the top 3 values and their indexes.
import numpy as numpy 
arr=numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Get the indexes of the top 3 values
top_3_indexes = numpy.argsort(arr)[-3:][::-1]
# Get the top 3 values using the indexes
top_3_values = arr[top_3_indexes]