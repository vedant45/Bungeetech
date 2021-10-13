import pandas as pd
df = pd.read_csv("..\..\input\question-1\main.csv")
df1 = df[['Year','Population','Violent','Property','Murder','Forcible_Rape','Robbery','Aggravated_assault','Burglary','Larceny_Theft','Vehicle_Theft']]
df1.set_index("Year", inplace = True)
df1.insert(0, "Decade", (df1.index//10)*10, True)
df2 = df1.groupby('Decade').sum()
df1 = df1.groupby('Decade').tail(1)
df3 = df1['Population'].to_list()
se = pd.Series(df3)
df2['Population'] = se.values
df2.rename(columns = {'Decade':'Year'}, inplace = True)
df2.to_csv('main.csv')
