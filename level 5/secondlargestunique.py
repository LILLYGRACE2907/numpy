#Find the second-largest unique value in a NumPy array.
import numpy as numpy
arr=numpy.array([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
unique_values = numpy.unique(arr)
print("Unique values in the array:", unique_values)
if len(unique_values) < 2:
    print("There is no second-largest unique value.")
else:
    second_largest = unique_values[-2]
    print("The second-largest unique value is:", second_largest)    