#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd
import numpy as np
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from matplotlib import figure as fig
import mplfinance as mpf
import math


# In[39]:


dataset=pd.read_csv('C:/Users/Sebi/Desktop/B.tech/GRIET/sem 6/mini proj/archive (1)/Data/DABUR.NS.csv')


# In[40]:


dataset.head()


# In[21]:


dataset['Date']=pd.to_datetime(dataset.Date)


# In[23]:


dataset.shape


# In[42]:


dataset.drop(,axis = 1, inplace = True)
dataset.head()


# In[28]:


dataset.isnull().sum()
dataset.isna().any()


# In[30]:


dataset.info()


# In[32]:


dataset.describe()


# In[34]:


print(len(dataset))


# In[52]:


print(dataset)
#mpf.plot(dataset,type='candle',style='charles')
dataset['Open'].plot(figsize=(16,6))


# In[55]:


x = dataset[['Open','High','Low','Volume']]
y= dataset['Close']
#print(x)


# In[74]:


from sklearn.model_selection import train_test_split
x_train , x_test , y_train, y_test =train_test_split(x , y, random_state=0)
#x_train.shape
#x_test.shape
print(y_test)


# In[64]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, accuracy_score
regressor=LinearRegression()
regressor.fit(x_train,y_train)


# In[67]:


print(regressor.coef_)


# In[69]:


print(regressor.intercept_)


# In[71]:


predicted=regressor.predict(x_test)
print(x_test)


# In[77]:


dframe=pd.DataFrame(y_test,predicted)
dfr=pd.DataFrame({'actual_price':y_test,'predicted_price':predicted})
print(dfr)


# In[79]:


from sklearn.metrics import confusion_matrix, accuracy_score
regressor.score(x_test,y_test)


# In[81]:


print('mean absolute error',metrics.mean_absolute_error(y_test,predicted))


# In[83]:


print('mean squared error',metrics.mean_squared_error(y_test,predicted))


# In[87]:


print('root mean squared error',math.sqrt(metrics.mean_absolute_error(y_test,predicted)))


# In[88]:


graph=dfr.head(20)
graph.plot(kind='bar')

