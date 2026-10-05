#. Find the column with the lowest average in a 2D array.
import numpy as numpy 
arr=numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Calculate the average of each column
column_averages = numpy.mean(arr, axis=0)
# Find the index of the column with the lowest average
lowest_average_index = numpy.argmin(column_averages)
# Print the index of the column with the lowest average
print("Column with the lowest average is at index:", lowest_average_index)