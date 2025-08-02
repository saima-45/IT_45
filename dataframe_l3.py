import pandas as pd
DF=pd.DataFrame()
print(DF)

print("------------------slide 8----------------------")

df=pd.DataFrame([11,22,33,44,55])
print(df)

print("-------------------slide 9,10---------------------")
daf = pd.DataFrame([11,22,33,44,55],index=['R1','R2','R3','R4','R5'],
                   columns=['C1'])
print(daf)

print("-------------------slide 11---------------------")
data=pd.DataFrame([[21,'X','A'],[32,'IX','A'],[23,'X','A'],[12,'XI','A']])
print(data)

print("-------------------slide 12---------------------")
dataf=pd.DataFrame([[21,'X','A'],[32,'IX','A'],[23,'X','A'],[12,'XI','A']],
                   index=['rec1','rec2','rec3','rec4'],columns=["rno","class","sec"])
print(dataf)

print("-------------------slide 13---------------------")
Df=pd.DataFrame({'rno':[21,28,31],'class':['IX','X','XI'],'sec':['B','A','C']})
print(Df)

print("-------------------slide 14---------------------")
dF=pd.DataFrame({'B_id':['B1','B8','B5'],'Sub':['Hindi','Math','Science'],
                 'Cost':[450,520,400]},index=['R1','R2','R3'])
print(dF)

print("-------------------slide 15,16---------------------")
datafr=pd.DataFrame([{'Ram':25,'Anil':29,'Simple':28},
                     {'Ram':21,'Anil':25,'Simple':23},
                     {'Ram':23,'Anil':18}],
                     index=['Term1','Term2','Term3'])
print(datafr)
print("-------------------slide 17,18,19,20---------------------")
s1=pd.Series([10,20,30,40])
s2=pd.Series([11,22,33,44])
s3=pd.Series([34,44,54,])
dframe=pd.DataFrame([s1,s2,s3],index=['r1','r2','r3'])
print(dframe)
print("-------------------slide 21,22,23,24,25---------------------")
import numpy as np
ar1=np.array([1,2,3,4])
ar2=np.array([10,20,30,40])
ar3=np.array([-23,-43,67,90])
DATAf=pd.DataFrame([ar1,ar2,ar3])
print(DATAf)
print("-----------------slide 26,27(adding column)-------------------")
dataFR=pd.DataFrame([{'Ram':25,'Anil':29,'Simple':28},
                     {'Ram':21,'Anil':25,'Simple':23},
                     {'Ram':23,'Anil':18,'Simple':26}],
                     index=['R1','R2','R3'])
print(dataFR)
dataFR['Amit']=[18,22,25]
print(dataFR)
dataFR['Parth']=[28,12,30]
print(dataFR)
print("-----------------slide 28,29(adding row)-------------------")
dataFrame=pd.DataFrame([{'Ram':25,'Anil':29,'Simple':28},
                     {'Ram':21,'Anil':25,'Simple':23},
                     {'Ram':23,'Anil':18,'Simple':26}],
                     index=['R1','R2','R3'])
print(dataFrame)
dataFrame.loc['R4']=[18,22,25]
print(dataFrame)
print("-----------------slide 30,31,(deleting row)-------------------")
dataFRAME=pd.DataFrame([{'Ram':25,'Anil':29,'Simple':28},
                     {'Ram':21,'Anil':25,'Simple':23},
                     {'Ram':23,'Anil':18,'Simple':26}],
                     index=['R1','R2','R3'])
print(dataFRAME)
print("------------------------")
dataFRAME=dataFRAME.drop(['R2','R1'],axis=0)
print(dataFRAME)
print("-----------------slide 32,33,34(deleting columns)-------------------")
dataFRAM=pd.DataFrame([{'Ram':25,'Anil':29,'Simple':28},
                     {'Ram':21,'Anil':25,'Simple':23},
                     {'Ram':23,'Anil':18,'Simple':26}],
                     index=['R1','R2','R3'])
print(dataFRAM)
print("------------------------")
print(dataFRAM.drop(['Simple','Ram'],axis=1))
print(dataFRAM)
print("-----------------slide 35,36(renaming row)-------------------")
dataFRA=pd.DataFrame([{'Ram':25,'Anil':29,'Simple':28},
                     {'Ram':21,'Anil':25,'Simple':23},
                     {'Ram':23,'Anil':18,'Simple':26}],
                     index=['R1','R2','R3'])
print(dataFRA)
dataFRA=dataFRA.rename({'R1':'Maths','R2':'Science','R3':'English'},
                       axis='index')
print("------------------------")
print(dataFRA)
print("-----------------slide 37,38(renaming column)-------------------")
dataFR=pd.DataFrame([{'Ram':25,'Anil':29,'Simple':28},
                     {'Ram':21,'Anil':25,'Simple':23},
                     {'Ram':23,'Anil':18,'Simple':26}],
                     index=['R1','R2','R3'])
print(dataFR)
dataFR=dataFR.rename({'Ram':'Ravi','Simple':'Sumit'},axis='columns')
print("------------------------")
print(dataFR)
print("-----------------slide 39,40-------------------")
datA=pd.DataFrame([[25,29,28],[21,25,23],[23,18,26]],
                  index=['R1','R2','R3'],
                  columns=['Ram','Anil','Simple'])
print(datA)
print("------------------------")
print(datA.loc[['R1','R3']])
print("-----------------slide 41-------------------")
daTA=pd.DataFrame([[25,29,28],[21,25,23],[23,18,26]],
                  index=['R1','R2','R3'],
                  columns=['Ram','Anil','Simple'])
print(daTA)
print("------------------------")
print(daTA['Ram'])
print("-----------------slide 42-------------------")
dATA=pd.DataFrame([[25,29,28],[21,25,23],[23,18,26]],
                  index=['R1','R2','R3'],
                  columns=['Ram','Anil','Simple'])
print(dATA)
print("------------------------")
print(dATA[['Ram','Anil']])
print("-----------------slide 43-------------------")
dATAF=pd.DataFrame([[25,29,28],[21,25,23],[23,18,26]],
                  index=['R1','R2','R3'],
                  columns=['Ram','Anil','Simple'])
print(dATAF)
print("------------------------")
print(dATAF.loc[:,'Ram'])
print("-----------------slide 44-------------------")
dATAFR=pd.DataFrame([[25,29,28],[21,25,23],[23,18,26]],
                  index=['R1','R2','R3'],
                  columns=['Ram','Anil','Simple'])
print(dATAFR)
print("------------------------")
print(dATAFR.loc[:,'Ram':'Anil'])
print("-----------------slide 45-------------------")
dATAFRA=pd.DataFrame([[25,29,28],[21,25,23],[23,18,26]],
                     index=['R1','R2','R3'],
                     columns=['Ram','Anil','Simple'])
print(dATAFRA)
print("---------------------")
print(dATAFRA.iloc[:, 0:1])
print("-----------------slide 46,47-------------------")
DATAFRA=pd.DataFrame([[25,29,28],[21,25,23],[23,18,26]],
                     index=['R1','R2','R3'],
                     columns=['Ram','Anil','Simple'])
print(DATAFRA)
print("---------------------")
print(DATAFRA.iloc[:, 1:2])
print("-----------------slide 48,49-------------------")
DATAFRAM=pd.DataFrame([[25,29,28,17],[21,25,23,20],[23,18,26,23],
                       [20,18,30,15]],
                     index=['R1','R2','R3','R4'],
                     columns=['Ram','Anil','Simple','Anuj'])
print(DATAFRAM)
print("---------------------")
print(DATAFRAM.loc[['R1','R2','R4']])
print("-----------------slide 50,51,52-------------------")
DATAFRAME=pd.DataFrame([[25,29,28,17],[21,25,23,20],[23,18,26,23],
                       [20,18,30,15]],
                     index=['Math','English','Science','Hindi'],
                     columns=['Ram','Anil','Simple','Anuj'])
print(DATAFRAME)
print("---------------------")
print(DATAFRAME.loc['Math':'Science',['Ram','Anil','Anuj']])
print("-----------------slide 53,54-------------------")
DATAFRAMe=pd.DataFrame([[25,29,28],[21,25,23],[23,18,26],
                       ],
                     index=['Math','English','Science'],
                     columns=['Ram','Anil','Simple'])
print(DATAFRAMe)
print("---------------------")
print(DATAFRAMe.loc[:, 'Anil']>25)
print("-----------------slide 55,58-------------------")
df1 = pd.DataFrame(
    [[25, 29, 28, 17], [21, 25, 23, 20], [23, 18, 26, 23], [20, 18, 30, 15], [12, 15, 20, 3], [23, 12, 16, 30]],
    index=['R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
    columns=['Ram', 'Anil', 'Simple', 'Anuj']
)
print(df1)
print("------------------------------------------")
df2 = pd.DataFrame(
    [[10, 12, 8, 7], [1, 5, 3, 2], [2, 1, 2, 2], [0, 1, 3, 5]],
    index=['R1', 'R2', 'R5', 'R6'],
    columns=['Ram', 'Anil', 'Ravi', 'Ashish']
)
print(df2)
print("------------------------------------------")
df1 = df1._append(df2,sort=True)
print(df1)

print("-----------------slide 59-------------------")
import pandas as pd
dframe = pd.DataFrame([[25, 29, 28, 17], [21, 25, 23, 20], [23, 18, 26, 23], [20, 18, 30, 15]], 
                  index=['R1', 'R2', 'R3', 'R4'], 
                  columns=['Ram', 'Anil', 'Simple', 'Anuj'])
print(dframe)
print("--------------------------------------------------")
print(dframe.index)
print("--------------------------------------------------")
print(dframe.columns)
print("--------------------------------------------------")
print(dframe.dtypes)
print("--------------------------------------------------")
print(dframe.shape)
print("--------------------------------------------------")
print(dframe.size)
print("--------------------------------------------------")
print(dframe.T)
print("--------------------------------------------------")
print(dframe.values)
print("--------------------------------------------------")
print(dframe.empty)
print("-----------------slide 62-------------------")
df3 = pd.DataFrame(
    [[25, 29, 28, 17], [21, 25, 23, 20], [23, 18, 26, 23], [20, 18, 30, 15], [12, 15, 20, 3], [23, 12, 16, 30]],
    index=['R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
    columns=['Ram', 'Anil', 'Simple', 'Anuj']
)
print(df3)
print("------------------------------------------")
print(df3.head(2))
print("------------------------------------------")
print(df3.head(1))  
print("------------------------------------------")
print(df3.head()) 
print("------------------------------------------")
print("--------------------slide 64-------------------------")
df4 = pd.DataFrame(
    [[25, 29, 28, 17], [21, 25, 23, 20], [23, 18, 26, 23], [20, 18, 30, 15], [12, 15, 20, 3], [23, 12, 16, 30]],
    index=['R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
    columns=['Ram', 'Anil', 'Simple', 'Anuj']
)
print(df4)
print("------------------------------------------")
print(df4.tail(2))
print("------------------------------------------")
print(df4.tail(1))  
print("------------------------------------------")
print(df4.tail()) 
print("------------------------------------------")

















