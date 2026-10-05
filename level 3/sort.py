#Sort a NumPy array.
import numpy as numpy
arr = numpy.array([[3, 7, 10], [40, 50, 60], [70, 80, 90]])
#Sort the array in ascending order
sorted_arr = numpy.sort(arr, axis=None)
print("Sorted array:", sorted_arr)
print("Original array:", arr)
print("Sorted array in descending order:", sorted_arr[::-1])
print("Original array in descending order:", arr[::-1])
print("Sorted array along axis 0:", numpy.sort(arr, axis=0))
print("Sorted array along axis 1:", numpy.sort(arr, axis=1))
print("Original array along axis 0:", arr)
print("Original array along axis 1:", arr)