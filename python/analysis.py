# %% enirov clean...importing latest clean file
import json
import csv
import pandas as pd
import matplotlib.pyplot as plt
#load raw data into raw
#raw = pd.read_csv("raw.csv")
#df = pd.DataFrame(raw)
clean = pd.read_csv("clean.csv")
df = pd.DataFrame(clean)
pd.set_option('max_columns', 5)
pd.set_option('max_rows', None)
df.tail()
study = df.groupby(['study-name', 'study-index'])

# %% data clean
# raw = pd.read_csv("raw.csv")
# df = pd.DataFrame(raw)
# df = df[df.user != 'UQA6D5YFR']
# df = df[df.user != 'UNPEBLGE4']
# df = df[df.subtype != 'channel_join']
# df.to_csv("clean.csv")


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
study = df.groupby(['study-index'])

study.get_group(5)
study['user'].value_counts().loc[4]
study['user'].value_counts(normalize = True).loc[4]
study['user'].value_counts(normalize = True)
#study['user'].value_counts().head()
study['text'].apply(lambda x: x.str.contains('the').sum())
# %%
df.columns
study = df.groupby(['study-index'])
study['text_word_count'].std()
study['user'].value_counts()

study = df.groupby(['study-name', 'study-index'])
study['user'].value_counts()

study['text_word_count'].std()
study['text_word_count'].sum()
# %% plot

#study['text_word_count'].sum().plot(kind = 'bar', title = 'Sum of Word Count Per Study')
study_by_user = df.groupby(['study-index', 'user'])
study['user'].value_counts()
study['user'].apply(lambda x: study[study['user' == x]]['text_word_count'].sum())



# %% NUMBER OF WORDS PER USER
# correct way to group by: study-index and user
study =  df.groupby(['study-index', 'user'])

sum_study = study['text_word_count'].agg({'sum': 'sum', 'mean': 'mean', 'std': 'std'})
keyword = 'std'
# sum_study[sum_study['study-index' == 4]]['std'].tail()
# sum_study['std'].unstack(level=0).plot(subplots=True, layout=(2, 3), kind = 'bar');
# sum_study.reset_index().pivot('study-index','user', 'std').plot( title='Var1', grid=True)

# sum_study['std'].unstack(level=1).plot(subplots=True, kind = 'bar');

# for df_select in sum_study.groupby(level=0):
#     df_select.plot(kind = 'bar')

# correct way to access mutilevel loc[5] = study-index 5
sum_study.loc[5][keyword]
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(10, 6))
fig.subplots_adjust(hspace=1)

index_list = [4, 7, 9, 5, 6, 8]
i = 0;
j = 0;
for x in index_list:
    if(i == 3):
        j = 1
        i = 0
    
    sum_study.loc[x].sort_values(keyword)[keyword].plot(kind = 'bar', ax=axs[j, i])
    fig.suptitle(keyword.capitalize() + ' of number of words per users')
    axs[j, i].set_title('Study {}'.format(x))
    i+=1

# %% HAS 'REACTION'
study['has reactions'].sum()
study['has reactions'].sum().plot(kind = 'bar')


# %% HAS 'REACTION'
study['has @'].sum()
study['has @'].sum().plot(kind = 'bar', title = 'Sum of msgs that has @ per study')

# %% has I/i/you/u
study['has I/i/you/u'].sum()
study['has I/i/you/u'].sum().plot(kind = 'bar', title = 'Sum of msgs that has  I/i/you/u per study')

# %% has I/i/you/u
study['has !'].sum()
study['has !'].sum().plot(kind = 'bar', title = 'Sum of msgs that has ! per study')


# %% short msg
study['short msg'].sum()

# %% long msg
study['long msg'].sum()

# %% word length
study['word length'].sum()
study['word length'].sum().plot(kind = 'bar', title = 'Sum of word length per study')

study['word length'].std()
study['word length'].std().plot(kind = 'bar', title = 'Std of word length per study')

# %% average word length
study['avg word length'].mean()
study['avg word length'].mean().plot(kind = 'bar', title = 'mean of avg word length per msg per study')

study['word length'].std().plot(kind = 'bar', title = 'std of avg word length per msg per study')
study['word length'].std()
# %% frequency of user
study =  df.groupby(['study-index', 'user'])
user_count = study['user'].count()



# %% acknowledgment_auto
study['acknowledgment_auto'].sum()
# study['acknowledgment_auto'].sum().plot(kind = 'bar', title = 'Sum of acknowledgment_auto per study')


# %%
