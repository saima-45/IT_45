import pandas as pd
print("question 1 & question 2")
ds = pd.Series([2,4,6,8,10])

print(ds)
print("pandas series and type")
print(ds)
print(type(ds))
print("pandas series as list")
print(ds.tolist())
print(type(ds.tolist()))

print("-------------------------------------")
print("question 3")

s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,9])
s=s1+s2
print("Add two series:")
print(s)
print("Subtract two series:")
s=s1-s2
print(s)
print("Multiply two series;")
s=s1*s2
print(s)
print("Divide series1 by series2:")
s=s1/s2
print(s)

print("-------------------------------------")
print("question 4")

import numpy as np
np_array =np.array([10,20,30,40,50])
print("NumPy array:")
print(np_array)
new_Series = pd.Series(np_array)
print("Converted pandas series:")
print(new_Series)

print("-------------------------------------")
print("Self practice")
print("Question 1")

vowels = pd.Series(["a","e","i","o","u"])
print(vowels)

print("-------------------------------------")
print("question 2")

a = (11, 22, 33, 44, 55)
series = pd.Series(a)
print(series)

print("-------------------------------------")
print("question 3")

name= input("Enter your name:")
name_series = pd.Series(list(name))
print(name_series)

print("-------------------------------------")
print("question 4")

D={"Jan":31,"Feb":28,"March":31,"April":30,"May":31,
   "June":30,"July":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}
month_series=pd.Series(D)
print(month_series)

print("-------------------------------------")
print("question 5")

class_students={6:10,7:20,8:30,9:40,10:50}
student_series=pd.Series(class_students)
print(student_series)

print("-------------------------------------")
print("question 6")

data=pd.Series({"A" : 25000,"B":12000,"C":8000,"D":5000})
data["D"]= 7000
print(data)

print("-------------------------------------")
print("question 7")

data_1=pd.Series({0:300,1:1200,2:1700,3:100})
data_2=data_1[data_1>200]
print(data_2)











