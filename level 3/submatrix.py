#Extract a 2×2 sub-matrix from a 4×4 matrix.
import numpy as numpy
arr=numpy.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])
sub_matrix=arr[1:3, 1:3]
print(sub_matrix)

