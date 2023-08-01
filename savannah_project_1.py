#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("/Users/olive/Desktop/Netflix Userbase.csv")
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


if df.duplicated().any():
    print("Duplicates found!")
else:
    print("No duplicates found.")


# In[5]:


df.drop(['User ID'],axis=1, inplace=True)
reduced_df = df[["Age", "Device"]]
reduced_df.head()


# In[12]:


df.Age.value_counts().plot(kind='bar',color='#203c15',figsize=(10,6))
plt.ylabel("User Count")
plt.xlabel("Age")
plt.show()


# In[7]:


df.Device.value_counts().plot(kind='pie',shadow='True' ,autopct='%1.2f%%', startangle = 75,figsize=(8,8))
plt.show()


# In[8]:


df['Age Groups'] = pd.cut(df['Age'], bins=[0, 18, 25, 35, 45, 100], labels=['<18', '18-24', '25-34', '35-44', '45+'])


# In[9]:


device_type = df.groupby('Device')

count_device_types = device_type['Device'].count()

count_device_types


# In[10]:


count_chart = count_device_types.plot(kind='bar', figsize=(6,8))

count_chart.set_xlabel("Device Type")
count_chart.set_ylabel("User count")

plt.show()
plt.tight_layout()


# In[ ]:




