import pandas as pd
df = pd.read_csv("..\..\input\question-3\main.csv")
df = df.sort_values(['Red Cards', 'Yellow Cards'], ascending = [False, False])
df1 = df[['Team','Yellow Cards','Red Cards']]
df1.to_csv('main.csv')