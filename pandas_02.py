# import pandas as pd
# import numpy as np 
# data = np.array(['a', 'b', 'c', 'd'])
# s = pd.Series(data)
# print("Pandas series")
# print(s)

# lst = ['Hey', 'there', '!', 'how', 'are', 'you']
# df = pd.DataFrame(lst)
# print(df)

##OPERATIONs IN PANDAS

import pandas as pd
df = pd.read_csv("data-.csv")
print(df.head())
df.info()

print(df.isnull().sum())
df = df.fillna(0)

ages = df[df['age']>25]
print(ages)

Sales = df[df['sales']>200]
print(Sales)

df['Total'] = df['a'] + df['b']
print(df.head())

res = df.groupby('category')['sales'].sum()
print(res)

import pandas as pd
data = [['Tom', 25], ['Krish', 30], ['Anjali', 20], ['Aditya', 18]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df)
df['Age'] = df['Age'].astype(float)
print(df)
