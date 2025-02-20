import pandas as pd

df = pd.read_csv('Inputs/data.csv')

dt = pd.DataFrame(columns=df.columns)

dt.loc[0] = df.iloc[10]

print(dt)


