import pandas as pd 

df = pd.read_csv("disc.csv")

cond = df['blacklist'].isin(df['whitelist'])
df.drop(df[cond].index, inplace = True)
df.to_csv('removed_dups.csv', encoding='utf-8', index=False)

