#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px
import plotly.offline as pyo


# ## INPUT THE DATASET

# In[5]:


df=pd.read_csv("covid_19_india.csv")
df.head()


# # DELETE COLUMNS

# In[12]:


del_1=['Sno','Time']
df.drop(del_1,axis=1,inplace=True)


# # ADD NEW COLUMN

# In[13]:


df['active_case']=df['Confirmed']-(df['Deaths']+df['Cured'])
df


# In[31]:


active_case=df['active_case'].sum()
print('Total no. of active cases in India',total_active)
t_c=df.groupby('State/UnionTerritory')['active_case'].sum().sort_values(ascending=False).to_frame()
t_c.style.background_gradient(cmap='Reds')


# #  How to see is there any missing value or not

# In[4]:


df.isnull().sum()


# In[5]:


df['State/UnionTerritory'].value_counts()


# In[4]:


df.style.background_gradient(cmap='Reds')


# # DATE VS CONFIRMED CASES

# In[5]:


plt.figure(figsize = (20,10))
figure = px.line(df, x='Date', y='Confirmed', color='State/UnionTerritory')
figure.update_xaxes(rangeslider_visible=True)
pyo.iplot(figure)


# #  DATE VS ACTIVE CASES

# In[7]:


plt.figure(figsize = (50,30))
figure = px.line(df, x='Date', y='active_case', color='State/UnionTerritory')
figure.update_xaxes(rangeslider_visible=True)
pyo.iplot(figure)


# #  DATE VS DEATHS

# In[6]:


plt.figure(figsize = (50,30))
figure = px.line(df, x='Date', y='Deaths', color='State/UnionTerritory')
figure.update_xaxes(rangeslider_visible=True)
pyo.iplot(figure)


# #  DATE VS CURED

# In[7]:


plt.figure(figsize = (50,30))
figure = px.line(df, x='Date', y='Cured', color='State/UnionTerritory')
figure.update_xaxes(rangeslider_visible=True)
pyo.iplot(figure)


# In[8]:


a=df.pivot_table(index='State/UnionTerritory',values=['Confirmed','Deaths','Cured','active_case'], aggfunc='median')
a=a.sort_values(by='Confirmed', ascending= False)
a


# # WEST BENGAL 

# In[1]:


wb=df[(df['State/UnionTerritory']=='West Bengal')&(df['State/UnionTerritory']=='Tamil Nadu')]
wb


# In[59]:


sns.jointplot(x='Date',y='Deaths',data=wb)


# In[51]:


g=sns.PairGrid(wb)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# #  WEST BENGAL DEATHS VS CURED

# In[13]:


sns.barplot(x="Cured",y='Deaths',data=wb)


# In[14]:


sns.distplot(wb['Deaths'])


# In[15]:


sns.distplot(wb['Deaths'],kde=False)


# #  INFO OF DATASET

# In[27]:


df.info()


# #  CORRELATION

# In[46]:


tc=df.corr()
tc


# In[44]:


sns.heatmap(tc)


# In[49]:


sns.heatmap(tc,annot=True,cmap='coolwarm')


# In[29]:


X = df.iloc[:,4:7].values
y = df.iloc[:, 7].values
print(X)
print(y)

