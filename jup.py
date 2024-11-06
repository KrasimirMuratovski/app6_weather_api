import numpy as np
import pandas as pd
import matplotlib as mp
df = pd.read_csv("data-small/TG_STAID000098.txt", skiprows=20, parse_dates=["    DATE"])
print(df[10:20])## show certain rows
print(df.columns)
print(df[['   TG','    DATE']])## return df with 2 columns
print(df['   TG'])## return df series

## Statistics and filtering
print(df['   TG'].mean())## applying mean on all the data
df.loc[df['   TG'] != -9999]## Returns the filtered df
df.loc[df['   TG'] != -9999]['   TG'].mean()

df['   TG'].hyst()
df.loc[df['    DATE'] == "1860-01-05"]['   TG'].squeeze()## temperature of a given day
df.loc[df['   TG'] == df['   TG'].max()]## max temp
df.loc[df['   TG'] == df['   TG'].max()]['    DATE'].squeeze()## the date of the max temp

## Transforming to NaN the invalid data
df["TG0"]=df['   TG'].mask(df['   TG']==-9999, np.nan)

## Calculate a new column out of existing
df["TG"] = df["TG0"]/10

##Plotting data
df.plot(x = '    DATE', y = 'TG', style = '.', figsize = (10,6))
df[100:200].plot(x = '    DATE', y = 'TG', style = '.', figsize = (10,6))