#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[39]:


import matplotlib.pyplot as plt


# In[336]:


data = pd.read_csv('Ruter_data.csv',names=['TurId', 'Dato', 'Fylke', 'Område', 'Kommune', 'Holdeplass_Fra', 'Holdeplass_Til', 'Linjetype', 'Linjefylke', 'Linjenavn', 'Linjeretning', 'Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra', 'Tidspunkt_Faktisk_Avgang_Holdeplass_Fra', 'Tidspunkt_Planlagt_Ankomst_Holdeplass_Fra', 'Tidspunkt_Planlagt_Avgang_Holdeplass_Fra', 'Kjøretøy_Kapasitet', 'Passasjerer_Ombord'])


# In[335]:


data.head()


# In[348]:


#First feature and visaulization: Bus capacity in relation of municipality
data.plot.scatter(x='Kjøretøy_Kapasitet', y='Kommune', title='Data over buss størrelsen', figsize= (20,10))
plt.grid()


# In[234]:


#Second feature and visualization: Number of stops in relation to area
fig,ax = plt.subplots()
ax.hist (data['Område'])
ax.set_title('Antall stopp per område')
ax.set_xlabel('Område')
ax.set_ylabel('Antall stopp')


# In[304]:


#Third feature: Number of lines per municipality
linje = data[['Kommune', 'Linjenavn']]
linje = linje.drop_duplicates(subset=['Linjenavn'])

linje = linje.groupby("Kommune")
linje = linje.agg({"Linjenavn": "nunique"})
linje = linje.reset_index()
linje.sort_values(by="Kommune")
linje.rename(columns={"Linjenavn": "Antall linjer"})



# In[322]:


#Visualizing third feature
fig, ax = plt.subplots(figsize=(10,3), dpi=100)
x = linje['Kommune']
y = linje ['Linjenavn']
plt.grid()
plt.bar(x, y)
plt.xticks(rotation=90)

ax.set_axisbelow(True)
ax.set_title('Antall linjer per kommune')
ax.set_xlabel('Kommune')
ax.set_ylabel('Antall linjer')


# In[347]:


#Feature 4: Which areas uses which line numebers
data.plot.scatter(x='Område', y='Linjenavn', title='Data over hvilke områder bruker hvilke linjer', figsize= (10,60))
plt.grid()


# In[356]:


#Feature 5: Which municipality uses which linetypes
data.plot.scatter(x='Kommune', y='Linjetype', title='Data over hvilke kommuner bruker hvilke linjetyper')
plt.grid()
plt.xticks(rotation=90)


# In[ ]:




