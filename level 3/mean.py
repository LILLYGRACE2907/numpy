#Replace values below the mean with the mean.
import numpy as numpy
arr=numpy.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
mean_value = numpy.mean(arr)
print("Mean value:", mean_value)
arr[arr < mean_value] = mean_value
print(arr)