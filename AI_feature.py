#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[39]:


import matplotlib.pyplot as plt


# In[291]:


data = pd.read_csv('Ruter_data.csv',names=['TurId', 'Dato', 'Fylke', 'Område', 'Kommune', 'Holdeplass_Fra', 'Holdeplass_Til', 'Linjetype', 'Linjefylke', 'Linjenavn', 'Linjeretning', 'Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra', 'Tidspunkt_Faktisk_Avgang_Holdeplass_Fra', 'Tidspunkt_Planlagt_Ankomst_Holdeplass_Fra', 'Tidspunkt_Planlagt_Avgang_Holdeplass_Fra', 'Kjøretøy_Kapasitet', 'Passasjerer_Ombord'])


# In[180]:


data.head()


# In[181]:


#First feature: Bus capacity in relation of county
data.plot.scatter(x='Kjøretøy_Kapasitet', y='Kommune', title='Data over buss størrelsen', figsize= (20,10))


# In[234]:


#Second feature: Number of stops in relation to area
fig,ax = plt.subplots()
ax.hist (data['Område'])
ax.set_title('Antall stopp per område')
ax.set_xlabel('Område')
ax.set_ylabel('Antall stopp')


# In[238]:


plt.pie(område_tall, )
plt.title('Antall stopp per område')


# In[186]:


data.plot.scatter(x='Område', y='Kjøretøy_Kapasitet', title='Liste over områdene', figsize= (20,10))


# In[252]:


data_passasjerer=data[(data['Passasjerer_Ombord']>0)]


# In[159]:


# create a figure and axis 
fig, ax = plt.subplots() 
# count the occurrence of each class 
data = data_passasjerer['Passasjerer_Ombord'].value_counts() 
# get x and y data 
Område = data.index 
Antall = data.values 
# create bar chart 
ax.bar(Område, Antall) 
# set title and labels 
ax.set_title('An Review Scores') 
ax.set_xlabel('Points') 
ax.set_ylabel('Frequency')


# In[292]:


data_kommune= (data['Kommune'])
data_kommune.head()


# In[297]:


data_kommune = data['Kommune'].unique()


# In[298]:


data_kommune


# In[ ]:


data_kommune 

