#Find the row with the highest sum in a 2D array.
import numpy as numpy
arr=numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_sums = numpy.sum(arr, axis=1)
max_row_index = numpy.argmax(row_sums)
print("Row with the highest sum is at index:", max_row_index)