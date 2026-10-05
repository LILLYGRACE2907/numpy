#Replace even values with 0 using boolean indexing.
import numpy as numpy
arr=numpy.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
arr[arr % 2 == 0] = 0
print(arr)