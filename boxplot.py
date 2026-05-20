import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\DIYA\OneDrive\Desktop\DSBDA-Practical\Ass07\studentPerformance.csv")
print("Demo Dataset:\n")
print(df.head())

# 2. Detect the outlier using BoxPlot
print("\nBoxPlot Before Handling Outliers:")
df.boxplot(column="math_score")
plt.show()

# Detect outliers in math_score using 10th and 90th percentile
lower_limit = df["math_score"].quantile(0.10)
upper_limit = df["math_score"].quantile(0.90)

print("\n10th Percentile Value (Lower Limit):", lower_limit)
print("90th Percentile Value (Upper Limit):", upper_limit)

# Find outliers
outliers = np.where((df["math_score"] < lower_limit) | (df["math_score"] > upper_limit))
print("\nOutlier Indexes:", outliers)

# Display outlier values
print("\nOutlier Values:")
print(df.loc[outliers[0], "math_score"])

# 3. Handle the outlier using Quantile based Flooring and Capping
# Values below 10th percentile are floored
# Values above 90th percentile are capped

df["math_score"] = np.where(df["math_score"] < lower_limit, lower_limit, df["math_score"])
df["math_score"] = np.where(df["math_score"] > upper_limit, upper_limit, df["math_score"])

print("\nDataset After Handling Outliers:\n")
print(df)

# BoxPlot after handling outliers
print("\nBoxPlot After Handling Outliers:")
df.boxplot(column="math_score")
plt.show()
