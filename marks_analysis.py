import numpy as np

marks = np.array([
    [85, 90, 88],
    [70, 75, 80],
    [95, 92, 96],
    [60, 65, 70]
])

print("Student Marks:\n")
print(marks)

average_marks = np.mean(marks, axis=1)

print("\nAverage Marks:")
print(average_marks)

topper = np.argmax(average_marks)

print(f"\nTopper Student Index: {topper}")

subject_average = np.mean(marks, axis=0)

print("\nSubject Wise Average:")
print(subject_average)

highest_mark = np.max(marks)

print(f"\nHighest Mark: {highest_mark}")
