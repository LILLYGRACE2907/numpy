#Extract all elements from the second row onward.
import numpy as numpy 
array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = array[1:, :]
print(result)