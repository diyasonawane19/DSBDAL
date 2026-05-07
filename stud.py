import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\DIYA\OneDrive\Desktop\DSBDA-Practical\Ass02\studentPerformance.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# 1. Missing values in whole dataframe
print("\n1. Any missing values in dataframe?")
print(df.isnull().values.any())

# 2. Missing values across each column
print("\n2. Missing values across each column:")
print(df.isnull().any())

# 3. Count of missing values across each column
print("\n3. Count of missing values in each column:")
print(df.isnull().sum())

# 4. Row-wise missing values count
print("\n4. Row-wise missing values count:")
print(df.isnull().sum(axis=1))

# 5. Missing values in gender column
print("\n5. Missing values in gender column:")
if 'gender' in df.columns:
    print(df['gender'].isnull().sum())
else:
    print("Gender column is not available in this dataset")

# 6. Groupby count of missing values
print("\n6. Groupby missing values count (club join year vs math_score):")
print(df.groupby('club join year')['math_score'].apply(lambda x: x.isnull().sum()))

# 7. Replace missing values in score column with average
print("\n7. Replace missing values in math_score with mean:")
df['math_score'] = df['math_score'].fillna(df['math_score'].mean())
print(df['math_score'])
