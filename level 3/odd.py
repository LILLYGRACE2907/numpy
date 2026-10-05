#Find all odd values using boolean indexing.
import numpy as numpy
arr=numpy.array([[3,7,10,], [40, 50, 60], [70, 80, 90]]) 
print(arr[arr % 2 != 0])