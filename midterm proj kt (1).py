#!/usr/bin/env python
# coding: utf-8

# In[19]:


import matplotlib.pyplot as plt
import json



elem=[2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,
6,8,9,10,6,7,4,3]
count={}
for item in elem:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
sorted_count=sorted(count.items())
for i in sorted_count:
    print(i[0],':', i[1])

x=list(count.keys())
y=list(count.values())
plt.xlabel('elememt')
plt.ylabel('frequency')
plt.bar(x,y)
plt.show()
y=json.dumps(sorted_count)
print (y)


# ## Question 2

# In[58]:


#Reading in data
import pandas as pd
df = pd.read_csv('amazon.csv')
df.head
df["Total charged"] = df["Total charged"].str.replace('$','').astype(float)
df.head
x = df["Total charged"].sum()
print('Total spent on amazon in period =',x,"$")
y = df["Total charged"].mean()
print('Average spent per day =', y,"$")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.head()
import matplotlib as plt
df.plot.bar(x = 'Order Date', y = 'Total charged', rot=90, figsize =(20,12))
daily_orders = df.groupby('Order Date').sum()["Total charged"]

daily_orders.head

daily_orders.plot.bar(figsize=(20,12), color = 'red')


# In[5]:


df


# In[25]:


len(df.Category.unique())


# # Breakdown by Category
# 
# 
# 

# In[100]:


Cats = df["Category"].value_counts()
import matplotlib.pyplot as plt
plt.figure(figsize=(22, 18))
plt.pie(Cats,labels=list(Cats.index.values))
plt.show()


# ## Monthly stats
# 

# In[95]:


df2 = df.set_index('Order Date', inplace=False)
sum_month=df2.groupby(pd.Grouper(freq='M'))['Total charged'].sum()
sum_month


# In[79]:


mmean = df2.groupby(pd.Grouper(freq='M'))['Total charged'].mean()
mmean.fillna(0, inplace = True)
mmean


# In[96]:


plt.figure(figsize=(10, 8))
plt.bar(list(sum_month.index.values),sum_month, width = 0.7)
plt.show()


# In[97]:


plt.figure(figsize=(10, 8))
plt.bar(list(mmean.index.values),mmean, width = 0.99)
plt.show()


# In[ ]:





# In[ ]:




