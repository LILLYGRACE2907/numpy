# Find the frequency of every unique value.
import numpy as numpy
arr=numpy.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
unique, counts = numpy.unique(arr, return_counts=True)
print("Unique values and their frequencies:")
for value, count in zip(unique, counts):
    print(f"Value: {value}, Frequency: {count}")
        