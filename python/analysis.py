# %% enirov setup
import json
import csv
import pandas as pd

#load raw data into raw
#raw = pd.read_csv("raw.csv")
#df = pd.DataFrame(raw)
clean = pd.read_csv("clean.csv")
df = pd.DataFrame(clean)
pd.set_option('max_columns', 5)
pd.set_option('max_rows', None)
# %% data clean

#df = df[df.user != 'UQA6D5YFR']
#df = df[df.user != 'UNPEBLGE4']
#df = df[df.subtype != 'channel_join']
#df.to_csv("clean.csv")


# %%
user_frq = df.groupby(['study-index','user']).count()
df = pd.DataFrame(user_frq)
df

# %% general tutorial
df[['study-index', 'user']]
df.columns
df.iloc[0]
df.loc[[0, 1], 'user'] #df.loc[n] access row
df.loc[[0, 1], ['user', 'text']]
df['user'].value_counts()
df.describe()
# %% grouping tutorial
df.groupby(['study-index'])


# %%
