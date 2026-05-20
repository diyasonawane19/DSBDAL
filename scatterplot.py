import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\DIYA\OneDrive\Desktop\DSBDA-Practical\Ass08\studentPerformance.csv")

print("Dataset:")
print(df.head())

# 2. Detect outliers using Scatter Plot
plt.scatter(df['Placement_score'], df['placement_count'])
plt.xlabel("Placement Score")
plt.ylabel("Placement Count")
plt.show()

# Find 10th and 90th percentile
low_score = df['Placement_score'].quantile(0.10)
high_score = df['Placement_score'].quantile(0.90)

low_count = df['placement_count'].quantile(0.10)
high_count = df['placement_count'].quantile(0.90)

# Detect outliers
outliers = np.where((df['Placement_score'] < low_score) | 
                    (df['Placement_score'] > high_score) |
                    (df['placement_count'] < low_count) | 
                    (df['placement_count'] > high_count))

print("Outlier Indexes:", outliers)

# 3. Handle outliers using flooring and capping
df['Placement_score'] = np.where(df['Placement_score'] < low_score, low_score, df['Placement_score'])
df['Placement_score'] = np.where(df['Placement_score'] > high_score, high_score, df['Placement_score'])

df['placement_count'] = np.where(df['placement_count'] < low_count, low_count, df['placement_count'])
df['placement_count'] = np.where(df['placement_count'] > high_count, high_count, df['placement_count'])

print("\nUpdated Dataset:")
print(df)

# Scatter Plot after handling outliers
plt.scatter(df['Placement_score'], df['placement_count'])
plt.xlabel("Placement Score")
plt.ylabel("Placement Count")
plt.show()
