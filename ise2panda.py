import pandas as pd
df = pd.read_csv("student.csv")
print("Missing values in each column:")
print(df.isnull().sum())
numeric_columns = df.select_dtypes(include="number").columns
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())
print("Missing values after filling:")
print(df.isnull().sum())
print(df.describe())
