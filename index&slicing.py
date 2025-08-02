import pandas as pd
print("Indexing")
print("---------------------------")
print("practical 1")
d=[31,15,17,20]
s2=pd.Series(d)
print(s2[2])
print(s2[0])

print("---------------------------")
print("practical 4")
e=[1,2,3]
S2=pd.Series(e,index=["one","two","three"])
print(S2[-1])
