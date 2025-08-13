print("1. Example to slice numpy array with index [1:5]")
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:5])

print("2. Example to slice 1D NumPy Array in steps")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr1[1:5:2])

print("1. Example to slice 2D numpy array with index [1, 1:3]")
arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr3[1, 1:3])

print("2. Example to slice 2D numpy array with index [0:2, 1:3]")
arr4 = np.array([[1,  2,  3,  4,  5],
                [6,  7,  8,  9,  10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])
print(arr4[0:2, 1:3])

print("Slicing 3-D NumPy Array")
arr5 = np.array([[[1,  2,  3,  4,  5],
                 [6,  7,  8,  9,  10]],
                [[11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20]]])

print(arr5[0, 1, 1:4])

print("1. Split array into 4 smaller arrays")
arr6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
output = np.array_split(arr6, 4)
print(output)

print("2. Split array at specific indices")
arr7 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
output = np.array_split(arr7, [3, 7])
print(output)

