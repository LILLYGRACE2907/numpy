#Use boolean indexing to find values between 20 and 80.
import numpy as numpy
arr=numpy.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]) 
print(arr[(arr > 20) & (arr < 80)])