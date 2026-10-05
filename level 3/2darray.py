#Sort each row of a 2D array.
import numpy as numpy
arr=numpy.array([[3, 7, 10], [40, 50, 60], [70, 80, 90]])
sorted_arr = numpy.sort(arr, axis=1)
print("Original array:")
print(arr)
print("Array with each row sorted:")
print(sorted_arr)