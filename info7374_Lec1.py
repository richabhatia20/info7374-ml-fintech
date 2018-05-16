
# coding: utf-8

# In[66]:


#!pip install pandas
#!pip install numpy
#!pip install matplotlib
#!pip install seaborn
#!pip install plotly
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import plotly as ptl
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go


# In[67]:


df=pd.read_excel('AMZN.xlsx')


# In[68]:


df.head()


# In[69]:


df['Price'] = (df['open']+df['close'])/2


# In[70]:


df.head()


# In[79]:


ptl.tools.set_credentials_file(username='rbh7', api_key='idrYJvKKdnWlmxsqnPcT')

#data = [Bar(x=df.date,
#            y=df.Price)]

#py.iplot(data, filename='jupyter-date-price-bar')


# In[73]:



# Create a trace
trace = go.Scatter(
    x = df.date,
    y = df.Price
)

data = [trace]

py.iplot(data, filename='date-price')


# In[74]:



# Create a trace
trace2 = go.Scatter(
    x = df.date,
    y = df.volume
)

data = [trace2]

py.iplot(data, filename='date-volume')


# In[78]:


df.Price.describe()

