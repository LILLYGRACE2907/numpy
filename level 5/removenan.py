#. Remove rows containing NaN values from a 2D array
import numpy as numpy
arr = numpy.array([[1, 2, numpy.nan], [4, 5, 6], [numpy.nan, 8, 9]])
# Remove rows containing NaN values
arr = arr[~numpy.isnan(arr).any(axis=1)]