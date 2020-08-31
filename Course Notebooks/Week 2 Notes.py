#!/usr/bin/env python
# coding: utf-8

# # The Series Data Structure

# In[1]:


import pandas as pd
get_ipython().run_line_magic('pinfo', 'pd.Series')


# In[3]:


animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)


# In[4]:


numbers = [1,2,3]
pd.Series(numbers)


# In[5]:


animals = ['Tiger', 'Bear', None]
pd.Series(animals)


# In[6]:


numbers = [1,2, None]
pd.Series(numbers)


# In[7]:


import numpy as np
np.nan == None


# In[9]:


np.isnan(np.nan)


# In[10]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[11]:


s = pd.Series(np.random.randint(0,1000,10000))
s.head()


# In[12]:


len(s)


# In[13]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary = 0\nfor item in s:\n    summary+=item')


# In[14]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary = np.sum(s)')


# In[16]:


s+=2
s.head()


# In[17]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\nfor label, value in s.iteritems():\n    s.loc[label]= value+2')


# In[18]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\ns+=2')


# In[19]:


s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s


# In[20]:


original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)


# In[21]:


original_sports


# In[22]:


all_countries


# In[23]:


all_countries.loc['Cricket']


# # Data Frames and Data Structure

# In[24]:


import pandas as pd

pur_1 = pd.Series({'Name': 'Aru', 'Item Purchased':'Guns', 'Cost':300})
pur_2 = pd.Series({'Name': 'James', 'Item Purchased': 'Bullets', 'Cost':20})
pur_3 = pd.Series({'Name': 'Johnah', 'Item Purchased': 'RPG', 'Cost': 20000})

df = pd.DataFrame([pur_1,pur_2,pur_3], index = ['Ammo Store 1', 'Ammo Store 2', 'Ammo store 3'])

df.head()


# In[26]:


df.loc['Ammo Store 1']


# In[30]:


df['Location'] = ['India','UK','Israel']
df


# In[33]:


df.drop('Ammo Store 1')


# In[34]:


df['Cost'] *= 0.8 #Apply 10% discount
print(df)


# In[38]:


df[df['Cost']==240]


# In[39]:


import requests
import io


# In[40]:


url = 'https://raw.githubusercontent.com/irJERAD/Intro-to-Data-Science-in-Python/master/ClassNotebooks/log.csv'
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

df.head()


# In[41]:


get_ipython().run_line_magic('pinfo', 'df.fillna')


# In[44]:


df = df.set_index('time')
df = df.sort_index()
df


# In[45]:


df = df.reset_index()
df = df.set_index(['time', 'user'])
df


# In[46]:


df = df.fillna(method='ffill')
df.head()


# In[ ]:




