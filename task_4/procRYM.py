import pandas as pd
import numpy as np

df = pd.read_csv('rymData.csv', sep=' ')
df['prat'] = df['prat'].apply(lambda x: int(x.replace(',','')))
print(df['artist'].value_counts()[:1])
print(df[['artist', 'rymrat']].groupby('artist').agg({'rymrat':'median'}).sort_values(by=['rymrat'])[-10:-1])
print(df[['artist', 'prat']].groupby('artist').agg({'prat':'sum'}).sort_values(by=['prat'])[-10:-1])