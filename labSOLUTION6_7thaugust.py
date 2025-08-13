print("Q. Print or show only 3 decimal places of the numpy array rand_arr.")
import numpy as np
rand_arr=np.random.random((5,3))
rand_arr=np.random.random([5,3])
np.set_printoptions(precision=3)
print(rand_arr[:4])

print("Q. Get the common items between a and b")
a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])
c=np.intersect1d(a,b)
print(c)

print("Q. From array a1 remove all items present in array b1")
a1=np.array([1,2,3,4,5])
b1=np.array([5,6,7,8,9])
c1=np.setdiff1d(a1,b1)
print(c1)

print("Q. Get the positions where elements of a2 and b2 match")
a2=np.array([1,2,3,2,3,4,3,4,5,6])
b2=np.array([7,2,10,2,7,4,9,4,9,8])
c2=np.where(a2 == b2)
print(c2)

print("Q. Get all items between 5 and 10 from a.")
a3=np.array([2, 6, 1, 9, 10, 3, 27])
index=np.where((a3>=5)&(a3<=10))
print("Method 1:")
print(a3[index])
index=np.where(np.logical_and(a3>=5,a3<=10))
print("Method 2:")
print(a3[index])
print("Method 3:")
print(a3[(a3>=5)&(a3<=10)])

print(" Q.Find the Sum of All Values in a NumPy Array")
array_values = np.array([[12, 45, 23], [67, 34, 89]])
total_sum = np.sum(array_values)
print("NumPy Array:\n", array_values)
print("\nSum of All Values in the Array:", total_sum)

print("Q.Create a NumPy Array of Floating-Point Numbers Between 0 and 1 with Shape (2, 3, 4).")
array_floats = np.random.rand(2, 3, 4)
print("3D NumPy Array with Random Floating-Point Numbers:\n", array_floats)

print("Q. Find the Maximum Value in a NumPy Array")
array_values = np.array([[12, 45, 23], [67, 34, 89]])
max_value = np.max(array_values)
print("NumPy Array:\n", array_values)
print("\nMaximum Value in the Array:", max_value)

print("Q. Find the Minimum Value in a NumPy Array")
array_value=np.array([[12,45,23],[67,34,89]])
min_value=np.min(array_value)
print("NumPy Array:\n", array_value)
print("\nMinimum value in the array:", min_value)

print("Q. Find the Median Value of a NumPy Array")
array_val= np.array([[10, 25, 15], [40, 35, 20]])
median_value = np.median(array_val)
print("NumPy Array:\n", array_val)
print("\nMedian Value of the Array:", median_value)

print("Q. Compute the Dot Product of Two NumPy Arrays")
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(array1, array2)
print("Array 1:\n", array1)
print("\nArray 2:\n", array2)
print("\nDot Product Result:\n", dot_product)

print("Q. Compute the Cross Product of Two NumPy Arrays")
array3 = np.array([1, 2, 3])
array4 = np.array([4, 5, 6])
cross_product = np.cross(array3, array4)
print("Array 3:", array1)
print("Array 4:", array2)
print("\nCross Product Result:", cross_product)

print("Q. Compute the Inverse of a NumPy Array")
array6 = np.array([[4, 7], [2, 6]])
inverse = np.linalg.inv(array6)
print("Original Array:\n", array6)
print("\nInverse of the Array:\n", inverse)

print("Q. Reversed Array ")
a = np.array([1, 2, 3, 4])
reversed_a = a[::-1]
print(reversed_a)

print("Q. Compute the Determinant of a NumPy Array")
array7 = np.array([[4, 6], [3, 8]])
determinant = np.linalg.det(array7)
print("Original Array:\n", array7)
print("\nDeterminant of the Array:", determinant)

print("Q.A Concatenate Two NumPy Arrays Horizontally and Vertically")
a1 = np.array([[1, 2], [3, 4]])
b1= np.array([[5, 6], [7, 8]])
result = np.hstack((a1, b1))
result1 = np.vstack((a1, b1))
print(result)
print(result1)

print("Q.A Sort a NumPy Array in Ascending Order?")
arr1 = np.array([[3, 1, 4, 2], [7, 8, 2, 0]])
sorted_arr = np.sort(arr1)
print(sorted_arr)

print("Q.A Sort a NumPy Array in Descending Order?")
arr2 = np.array([[3, 1, 4, 2], [0, 9, 2, 5]])
sorted_arr = np.sort(arr2)[:, ::-1]
print(sorted_arr)
















