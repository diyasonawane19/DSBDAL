import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Species']
iris = pd.read_csv(csv_url, header=None, names=col_names)

# Display first 5 rows
print("Original Dataset:")
print(iris.head())

print("\n===== Label Encoding =====")

label_encoder = LabelEncoder()
iris_label = iris.copy()
iris_label['Species_Label'] = label_encoder.fit_transform(iris_label['Species'])

print(iris_label[['Species', 'Species_Label']].head(10))

print("\n===== One-Hot Encoding =====")

onehot_encoder = OneHotEncoder(sparse_output=False)
onehot = onehot_encoder.fit_transform(iris[['Species']])

onehot_df = pd.DataFrame(
    onehot,
    columns=onehot_encoder.get_feature_names_out(['Species'])
)

iris_onehot = pd.concat([iris.drop(columns=['Species']), onehot_df], axis=1)

print(iris_onehot.head())

print("\n===== Dummy Encoding =====")

iris_dummy = pd.get_dummies(iris, columns=['Species'])

print(iris_dummy.head())
