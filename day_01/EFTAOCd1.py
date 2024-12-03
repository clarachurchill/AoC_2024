import pandas as pd
df = pd.read_csv('day_01/aocd1.csv')
df1 = df.drop(columns=['col_2'])
df2 = df.drop(columns=['col_1'])

df1 = df1.sort_values(by=['col_1']).reset_index(drop = True)
df2 = df2.sort_values(by=['col_2']).reset_index(drop = True)

df3 = df1.join(df2)

df3['calc'] = abs(df3['col_1'] - df3['col_2'])
df3 = df3.drop(columns = ['col_1', 'col_2'])

total = df3.sum().sum()

df4 = df

occurance1 = []
occurance2 = []

for x in df4['col_1']:
    occurance1.append(df['col_2'].value_counts().get(x))

df4['Occurance1'] = occurance1

df4['Score1'] = df4['col_1']*df4['Occurance1']

df5 = df4.drop(columns = ['col_1', 'col_2', 'Occurance1'])
total2 = df5.sum().sum()

print(total2)