# Calculate row-wise and column-wise mean for a matrix.
import numpy as numpy
arr = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Calculate row-wise mean
row_mean = numpy.mean(arr, axis=1)
# Calculate column-wise mean
col_mean = numpy.mean(arr, axis=0)