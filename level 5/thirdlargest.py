#87. Find the third-largest value without sorting the entire array.
import numpy as numpy 
arr=numpy.array([10, 4, 3, 50, 23, 90])
def third_largest(arr):
    first = second = third = float('-inf')
    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif first > num > second:
            third = second
            second = num
        elif second > num > third:
            third = num
    return third if third != float('-inf') else None

print("The third-largest value is:", third_largest(arr))