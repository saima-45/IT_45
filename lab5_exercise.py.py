import numpy as np
print(np.__version__)
print("----Q.2 Create a 1D array of numbers from 0 to 9----")
arr = np.arange(10)
print(arr)
print("----Q.3 Create a 3×3 numpy array of all True’s----")
bool_arr = np.ones((3, 3),dtype=bool)
print(bool_arr)
print("----Q.4 Extract all odd numbers from arr----")
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd = array[array % 2 == 1]
print(odd)
print("----Q.5 Replace all odd numbers in arr with -1----")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1
print(arr)
print("----Q.6 Replace all odd numbers in arr with -1 without changing arr----")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = arr.copy()
out[out % 2 == 1] = -1
print(out)
print(arr)  
print("----Q.7 Convert a 1D array to a 2D array with 2 rows----")
a = np.arange(10)
reshaped = a.reshape(2, 5)
print(reshaped)
print("----Q.8 Get all items between 5 and 10 from a.----")
a = np.array([2, 6, 1, 9, 10, 3, 27])
result = a[(a >= 5) & (a <= 10)]
print(result)
print("----Q.9 Swap columns 1 and 2 in the array arr.----")
Array=np.array([[0, 1, 2,],
                [3, 4, 5],
                [6, 7, 8]])
print(Array)
Array = np.arange(9).reshape(3, 3)
Array = Array[:, [0,2, 1]]
print(Array)
print("----Q.10 Swap rows 1 and 2 in the array arr:----")
print(Array)
Array = np.arange(9).reshape(3, 3)
Array = Array[[0,2, 1], :]
print(Array)
print("----Q.11 Print or show only 3 decimal places of the numpy array rand_arr.----")
rand_arr = np.random.rand(3,3) * 10
print(np.round(rand_arr, 3))























