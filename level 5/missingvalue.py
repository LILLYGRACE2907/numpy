#Find the percentage of missing values represented by NaN.
import numpy as numpy
arr=numpy.array([1, 2, numpy.nan, 4, 5])
# Calculate the percentage of missing values
missing_percentage = numpy.isnan(arr).sum() / len(arr) * 100
print("Percentage of missing values:", missing_percentage)