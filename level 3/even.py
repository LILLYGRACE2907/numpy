#Find all even values using boolean indexing.
import numpy as numpy
arr=numpy.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]) 
print(arr[arr % 2 == 0])