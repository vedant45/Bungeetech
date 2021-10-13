import pandas as pd
df = pd.read_csv("..\..\input\question-2\main.csv")
df1 = df.groupby('occupation').agg({'age': [ 'min', 'max']})
df1.to_csv('main.csv')