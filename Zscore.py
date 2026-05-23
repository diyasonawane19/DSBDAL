import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Load the demo dataset in dataframe object df
df = pd.read_csv(r"C:\Users\DIYA\OneDrive\Desktop\DSBDA-Practical\Ass09\studentPerformance.csv")

print("Dataset:")
print(df.head())

# 2. Detect outliers using Z-score
z = np.abs(stats.zscore(df['math_score']))   # calculate z-score

print("\nZ-Score Values:")
print(z)

# Plot Z-score
plt.plot(z)
plt.title("Z-Score Plot")
plt.show()

# Find outliers
threshold = 2.5
outliers = np.where(z > threshold)

print("\nOutlier Indexes:", outliers)
print("Outlier Values:")
print(df.loc[outliers[0], 'math_score'])

# 3. Replace outliers with median value
median_value = df['math_score'].median()
print("\nMedian Value:", median_value)

df['math_score'] = np.where(z > threshold, median_value, df['math_score'])

print("\nUpdated Dataset:")
print(df)
