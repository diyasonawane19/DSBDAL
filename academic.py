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

df = pd.DataFrame(df)

print("Academic Performance Dataset:")
print(df)

print("------------------------")

# 2. Check null values in the dataset
print("Null Values in Dataset:")
print(df.isnull())

print("------------------------")

# 3. Count number of null values in complete dataset
df.replace(["?", "NA", "null", " "], np.nan, inplace=True)

print("Count of Null Values in Each Column:")
print(df.isnull().sum())

print("------------------------")
print("Total Null Values in Complete Dataset:")
print(df.isnull().sum().sum())

print("------------------------")

# 4. Dropping rows with at least 1 null value
print("Dataset after dropping rows with at least 1 null value:")
print(df.dropna())

print("------------------------")

# 5. Dropping rows if all values in that row are missing
print("Dataset after dropping rows where all values are missing:")
print(df.dropna(how='all'))

print("------------------------")

# 6. Dropping columns with at least 1 null value
print("Dataset after dropping columns with at least 1 null value:")
print(df.dropna(axis=1))
