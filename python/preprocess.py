# %% enirov setup
import json
import csv
import pandas as pd

# %% 

data = pd.read_json('../raw/7.json')
# f = csv.writer(open("test.csv", "wb+"))
data.to_csv("7.csv", encoding = 'utf-8')

data = pd.read_json('../raw/4.json')
# f = csv.writer(open("test.csv", "wb+"))
data.to_csv("4.csv", encoding = 'utf-8')


data = pd.read_json('../raw/5.json')
# f = csv.writer(open("test.csv", "wb+"))
data.to_csv("5.csv", encoding = 'utf-8')


data = pd.read_json('../raw/6.json')
# f = csv.writer(open("test.csv", "wb+"))
data.to_csv("6.csv", encoding = 'utf-8')


data = pd.read_json('../raw/8.json')
# f = csv.writer(open("test.csv", "wb+"))
data.to_csv("8.csv", encoding = 'utf-8')


data = pd.read_json('../raw/9.json')
# f = csv.writer(open("test.csv", "wb+"))
data.to_csv("9.csv", encoding = 'utf-8')


# %% import csv into dataframe
study4 = pd.read_csv("4.csv") 
col = study4['study-index'] = 4
study4.drop(labels=['study-index'], axis=1,inplace = True)
study4.insert(0, 'study-index', col)

study5 = pd.read_csv("5.csv") 
col = study5['study-index'] = 5
study5.drop(labels=['study-index'], axis=1,inplace = True)
study5.insert(0, 'study-index', col)

study6 = pd.read_csv("6.csv") 
col = study6['study-index'] = 6
study6.drop(labels=['study-index'], axis=1,inplace = True)
study6.insert(0, 'study-index', col)

study7 = pd.read_csv("7.csv") 
col = study7['study-index'] = 7
study7.drop(labels=['study-index'], axis=1,inplace = True)
study7.insert(0, 'study-index', col)

study8 = pd.read_csv("8.csv") 
col = study8['study-index'] = 8
study8.drop(labels=['study-index'], axis=1,inplace = True)
study8.insert(0, 'study-index', col)

study9 = pd.read_csv("9.csv") 
col = study9['study-index'] = 9
study9.drop(labels=['study-index'], axis=1,inplace = True)
study9.insert(0, 'study-index', col)

# %%
raw = pd.concat([study4, study5, study6, study7, study8, study9])

temp_xlsx = pd.DataFrame(raw)
temp_xlsx.to_csv('raw.csv')


# %%
raw = pd.read_csv("raw.csv")
df = pd.DataFrame(raw)
pd.set_option('max_columns', 5)
pd.set_option('max_rows', None)

df = df[df.user != 'UQA6D5YFR']
df = df[df.user != 'UNPEBLGE4']
df = df[df.subtype != 'channel_join']

user_frq = df.groupby(['study-index','user']).count()
df = pd.DataFrame(user_frq)


df
# %%
#pd.DataFrame(user_frq)['Unnamed: 0'].groupby(['study-index']).plot.barh()
# 4 - 10 
# 5 - 5
# 6 - 5 
# 7 - 10
# 8 - 5
# 9 - 10

pd.DataFrame(user_frq)['Unnamed: 0'].groupby(['study-index'])
pd.DataFrame(user_frq)['Unnamed: 0'].groupby(['study-index']).std().plot.barh()
pd.DataFrame(user_frq)['Unnamed: 0'].groupby(['study-index']).std()


# %%
pd.DataFrame(user_frq)['Unnamed: 0'].groupby(['study-index']).plot.barh()
pd.DataFrame(user_frq)['Unnamed: 0']


# %%
df = pd.DataFrame(raw)
pd.set_option('max_columns', 5)
pd.set_option('max_rows', None)

df = df[df.user != 'UQA6D5YFR']
df = df[df.user != 'UNPEBLGE4']
df = df[df.subtype != 'channel_join']
df['user'].hist(by=df['study-index'])

# %% data clean

