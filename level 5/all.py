#Create a 10×10 random matrix and find its minimum, maximum, mean, and standard deviation
import numpy as numpy
arr = numpy.random.rand(10, 10)
min_value = numpy.min(arr)
max_value = numpy.max(arr)
mean_value = numpy.mean(arr)
std_dev = numpy.std(arr)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
print("Mean value:", mean_value)
print("Standard deviation:", std_dev)