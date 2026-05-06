import numpy as np
import pandas as pd

# Step 1: Load dataset
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(csv_url, header=None)

# Step 2: Add column names
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
iris = pd.read_csv(csv_url, names=col_names)

# a) Display total rows and columns
print("Shape of dataset:")
print(iris.shape)

# b) Display datatype of each column
print("\nData types of each column:")
print(iris.dtypes)

# c) Sort data in descending order by Sepal_Length
print("\nSorted data (Descending by Sepal_Length):")
print(iris.sort_values(by='Sepal_Length', ascending=False))

# d) Slice rows 11 to 20 with Sepal_Length and Species
print("\nRows 11 to 20 with Sepal_Length and Species:")
print(iris.loc[11:20, ['Sepal_Length', 'Species']])

# e) Rename Species to Type
iris.rename(columns={'Species':'Type'}, inplace=True)

print("\nDataset after renaming Species to Type:")
print(iris.head())
