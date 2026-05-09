import pandas as pd
import numpy as np

# 1. Load the Academic Performance dataset in data frame object
df = {
    'Math_Score':[78,72,np.nan,69,80,75,np.nan,70,76,74],
    'Reading_Score':[85,88,90,np.nan,92,86,84,89,np.nan,87],
    'Writing_Score':[80,76,79,74,81,78,72,77,75,79],
    'Placement_Score':[90,85,88,82,95,89,80,87,91,86],
    'Club_Join_Date':['2019-06-12','2020-07-15','2018-08-20','2021-01-10',
                      '2019-03-18','2020-11-25','2021-05-30','2018-09-14',
                      '2019-12-05','2020-02-22'],
    'Place':['Nashik','Mumbai','Pune',np.nan,'Nashik','Mumbai',np.nan,'Pune','Nashik',np.nan]
}

df = pd.DataFrame(df, columns=['Math_Score','Reading_Score','Writing_Score',
                               'Placement_Score','Club_Join_Date','Place'])

print("Academic Performance Dataset:")
print(df)

print("------------------------")

# 2. Check null values in the dataset
print("Null Values in Dataset:")
print(df.isnull())

print("------------------------")
print("Column wise True / False:")
print(df.isnull().any())

print("------------------------")
print("Count of Null Values:")
print(df.isnull().sum())

print("------------------------")

# 3. Replace missing values with standard null value NaN
df.replace(["?", "NA", "null", " "], np.nan, inplace=True)

print("Dataset after replacing missing values with NaN:")
print(df)

print("------------------------")

# 4. Replace missing value of Math Score with Mean Value
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].mean())

# 5. Replace missing value of Reading Score with Standard Deviation
df['Reading_Score'] = df['Reading_Score'].fillna(df['Reading_Score'].std())

# 6. Replace missing value of Place with common value "Nashik"
df['Place'] = df['Place'].fillna("Nashik")

print("Updated Dataset after handling missing values:")
print(df)

print("------------------------")
print("Final Null Values Count:")
print(df.isnull().sum())
