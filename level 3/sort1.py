#Sort each column of a 2D array.
import numpy as numpy
arr=numpy.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
sorted_arr = numpy.sort(arr, axis=0)
print("Original array:")
print(arr)
print("Array with each column sorted:")
print(sorted_arr)