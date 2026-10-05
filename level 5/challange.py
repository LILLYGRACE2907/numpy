#Final Challenge: Build a NumPy Student Marks Analyzer. Given a 2D array of student marks, calculate total marks, average marks, highest and lowest scorer, subject-wise average, pass/fail count, grades, rank, and students above the class average.
import numpy as numpy
arr=numpy.array([[85, 90, 78], [92, 88, 95], [76, 85, 80], [89, 92, 91], [70, 75, 80]])
# Calculate total marks for each student
total_marks = numpy.sum(arr, axis=1)
# Calculate average marks for each student
average_marks = numpy.mean(arr, axis=1)
# Find the highest scorer
highest_scorer_index = numpy.argmax(total_marks)
# Find the lowest scorer
lowest_scorer_index = numpy.argmin(total_marks)
# Calculate subject-wise average
subject_average = numpy.mean(arr, axis=0)
# Count pass/fail (assuming pass mark is 40)
pass_count = numpy.sum(arr >= 40, axis=0)
fail_count = numpy.sum(arr < 40, axis=0)