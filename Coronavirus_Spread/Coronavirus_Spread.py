#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Progress Map
# #### Author: Ryan Julian
# 
# The goal of this project is to generate a gif displaying the progress of the 2019 novel coronavirus COVID-19.  The data for this project comes from the Johns Hopkins University Center for Systems Science and Engineering GitHub repository here: https://github.com/CSSEGISandData/COVID-19

# ## Packages

# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import imageio


# ## Data Intake
# 
# We use pandas to load the csv files containing COVID-19 time series data.  These files contain the numbers of confirmed cases, recoveries, and deaths due to coronavirus organized according to location and date.  The location data is typically resolved down to the province or country level, but in some regions such as the US, it is given by county.  Each location also comes with latitude and longitude values that are useful for displaying this data on our map.

# In[22]:


HEADER = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

covid_conf = pd.read_csv(HEADER+'time_series_19-covid-Confirmed.csv')
covid_rec = pd.read_csv(HEADER+'time_series_19-covid-Recovered.csv')
covid_death = pd.read_csv(HEADER+'time_series_19-covid-Deaths.csv')


# ## Making the Frames
# 
# Here we prepare a png image for each date currently in the dataset, and save these in a folder for later retrieval.  On top of a background world map, we display blue circles representing active cases at each location (confirmed - recovered - deaths) and red circles representing the total number of deaths at each location.  The size of the circles corresponds to the number of cases as indicated in the legend.

# In[23]:


i = 0
for date in covid_conf.keys()[4:]:
    m,d,y = date.split('/')
    d = '0'*(2-len(d))+d
    fig, ax = plt.subplots(figsize=(10,5))
    earth = Basemap(ax=ax)
    earth.drawcoastlines(color='#555555', linewidth=1)
    ax.scatter(covid_conf['Long'], covid_conf['Lat'], alpha = 0.2,
                    s = covid_conf[date]-covid_rec[date]-covid_death[date],c='blue')
    ax.scatter(covid_conf['Long'], covid_conf['Lat'], alpha = 0.2, 
              s = covid_death[date], c='red')
    ax.set_xlabel("COVID19 cases as of "+m+'/'+d+'/'+y)
    plt.scatter([],[], s=10, c='blue', alpha = 0.2, label='10 active cases')
    plt.scatter([],[], s=100, c='blue', alpha = 0.2, label='100 active cases')
    plt.scatter([],[], s=10, c='red', alpha = 0.2, label='10 deaths')
    plt.scatter([],[], s=100, c='red', alpha = 0.2, label='100 deaths')
    plt.legend(loc='lower left')
    i += 1
    filename = 'frame'+'0'*(3-len(str(i)))+str(i)+'.png'
    plt.savefig('png_images/'+filename,dpi=96)
    plt.close()


# ## Creating the gif
# 
# We use the imageio package to construct a gif from these frames.  The final frame is added to the end 30 extra times to give the viewer a few seconds to inspect the most recent map before the gif repeats.

# In[24]:


images = []
for j in range(1,i+1):
    images.append(imageio.imread('png_images/frame'+'0'*(3-len(str(j)))+str(j)+'.png'))
for j in range(1,30):
    images.append(imageio.imread('png_images/frame'+'0'*(3-len(str(i)))+str(i)+'.png'))
imageio.mimsave('COVID19.gif', images)


# In[ ]:




