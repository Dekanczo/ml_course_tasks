import pandas as pd
import numpy as np

pd.options.display.max_rows = 1000


df = pd.read_csv('rymData.csv', sep=' ')
df['prat'] = df['prat'].apply(lambda x: int(x.replace(',','')))
print(df['artist'].value_counts()[0:1], '\n')
print(df[['artist', 'prat']].groupby('artist').agg({'prat':'sum'}).sort_values(by=['prat'], ascending = True)[-1:None], '\n')
print(df[['artist', 'rymrat']].groupby('artist').agg({'rymrat':'median'}).sort_values(by=['rymrat'])[-10:None], '\n')