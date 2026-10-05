#Access the first element of a NumPy array.
import numpy as numpy
arr = numpy.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(arr[0])
print(arr[1])
#Access the last element using negative indexing.
print(arr[-1])
#Access the second row of a 2D array.
print(arr[1, :])
#Access the second column of a 2D array.
print(arr[:, 1])
#Access the third column of a 2D array.
print(arr[:, 2])
#Use slicing to extract the first three elements.
print(arr[0, :3])
#Reverse a NumPy array using slicing.
print(arr[::-1])