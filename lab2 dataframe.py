import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print("--------------------A.QUESTION 1-----------------------")
df = pd.DataFrame(exam_data, index=labels)
print(df)
print("--------------------A.QUESTION 2-----------------------")
df.loc[df['name'] == 'James', 'name'] = 'Suresh'
print(df)
print("--------------------A.QUESTION 3-----------------------")
df['age'] = [22, 23, 21, 24, 25, 26, 23, 24, 21, 22]
print("\nDataFrame after Inserting 'age' Column:")
print(df)
print("--------------------A.QUESTION 4-----------------------")
column_headers = df.columns.tolist()
print("\nColumn Headers as List:")
print(column_headers)
print("--------------------A.QUESTION 1-----------------------")
print("\nDefault Index:")
print(df.index)
df.set_index('name', inplace=True)
print("\nDataFrame with 'name' as Index:")
print(df)
print("--------------------A.QUESTION 2-----------------------")
df.index = pd.Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='int64')
print("\nDataFrame with 64-bit Integer Index:")
print(df)
df.index = pd.Index([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10], dtype='float64')
print("\nDataFrame with Floating-Point Number Index:")
print(df)
print("--------------------A.QUESTION 3-----------------------")
df['name_upper'] = df['name'].str.upper()
df['name_lower'] = df['name'].str.lower()

df['name_length'] = df['name'].str.len()

print("\nDataFrame after Converting Names to Upper/Lower Case and Length Calculation:")
print(df)
print("--------------------A.QUESTION 4-----------------------")
df['name_no_whitespace'] = df['name'].str.strip()  
df['name_no_left_whitespace'] = df['name'].str.lstrip()
df['name_no_right_whitespace'] = df['name'].str.rstrip()

print("\nDataFrame after Removing Whitespaces from Name Column:")
print(df)
print("--------------------A.QUESTION 5-----------------------")
exam_data2 = {
    'name': ['John', 'Alice', 'Bob'],
    'score': [14.5, 13, 15],
    'attempts': [2, 1, 3],
    'qualify': ['yes', 'no', 'yes']
}
labels2 = ['k', 'l', 'm']

df2 = pd.DataFrame(exam_data2, index=labels2)

df_combined = pd.concat([df, df2])
print("\nCombined DataFrame After Joining Along Rows:")
print(df_combined)
print("--------------------A.QUESTION 6-----------------------")
new_data = [{'name': 'Sara', 'score': 18, 'attempts': 1, 'qualify': 'yes'}, 
            {'name': 'Mark', 'score': 16, 'attempts': 2, 'qualify': 'no'}]

df_appended = df.append(new_data, ignore_index=True)
print("\nDataFrame After Appending List of Dictionaries:")
print(df_appended)
print("--------------------A.QUESTION 7-----------------------")
df1 = pd.DataFrame({
    'name': ['Anastasia', 'Dima', 'Katherine'],
    'score': [12.5, 9, 16.5]
})

df2 = pd.DataFrame({
    'name': ['Anastasia', 'Katherine', 'Dima'],
    'qualify': ['yes', 'yes', 'no']
})

df_merged = pd.merge(df1, df2, on='name')
print("\nMerged DataFrame with Matching Records:")
print(df_merged)

print("--------------------------------------------------------------")

# 1. Create DataFrame from Dictionary and Display It
data = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}
df = pd.DataFrame(data)
print(df)

# 2. Create DataFrame from Specified Dictionary Data with Index Labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df_exam = pd.DataFrame(exam_data, index=labels)
print(df_exam)

# 3. Get the First 3 Rows of the Given DataFrame
first_3_rows = df_exam.head(3)
print(first_3_rows)

# 4. Select the 'name' and 'score' Columns
selected_columns = df_exam[['name', 'score']]
print(selected_columns)

# 5. Select the Specified Columns and Rows
specified_rows_cols = df_exam.loc[['a', 'c', 'e'], ['name', 'score']]
print(specified_rows_cols)

# 6. Select Rows Where the Number of Attempts is Greater Than 2
rows_attempts_gt_2 = df_exam[df_exam['attempts'] > 2]
print(rows_attempts_gt_2)

# 7. Count the Number of Rows and Columns
num_rows, num_columns = df_exam.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# 8. Select Rows Where the Score is Missing (NaN)
rows_with_missing_scores = df_exam[df_exam['score'].isna()]
print(rows_with_missing_scores)
