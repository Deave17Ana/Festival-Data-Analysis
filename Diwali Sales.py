#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as ply
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[31]:


data = pd.read_csv('/Users/devanshverma/Downloads/Diwali Sales Data.csv',encoding = 'unicode_escape')


# In[32]:


data.shape


# In[33]:


data.head(5)


# In[34]:


data.info()


# In[35]:


data.isnull().sum()


# In[42]:


data.drop(['Status','unnamed1'],axis =1,inplace=True)


# In[45]:


data.info()


# In[46]:


data.isnull().sum()


# In[47]:


data.dropna(inplace=True)


# In[48]:


data.shape


# In[49]:


data.dtypes


# In[51]:


data['Amount']=data['Amount'].astype('int')


# In[52]:


data.dtypes


# In[55]:


data.columns


# In[56]:


data.describe()


# In[57]:


data.columns


# In[62]:


MF = sns.countplot(data=data, x='Gender')
for bar in MF.containers:
    MF.bar_label(bar)


# In[65]:


Age_grp = sns.countplot(data=data,x='Age Group',hue='Gender')
for bar in Age_grp.containers:
    Age_grp.bar_label(bar)


# In[70]:


sale_state = data.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(data=sale_state, x='State',y='Orders')


# In[ ]:




