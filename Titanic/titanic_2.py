from pandas import read_csv
from pandas import cut


titanic_df = read_csv("titanic.csv")

class_counts = titanic_df["PClass"].value_counts().sort_index()
print(class_counts)

print(titanic_df.groupby("PClass")["Survived"].mean())

print(titanic_df["Sex"].value_counts().sort_index())

print(titanic_df.groupby("Sex")["Survived"].mean())

print(titanic_df.groupby(["PClass", "Sex"])["Survived"].mean())

titanic_df['AgeGroup'] = cut(titanic_df['Age'], bins=[i * 10 for i in range(8)])
print(titanic_df.groupby("AgeGroup")["Survived"].mean())
