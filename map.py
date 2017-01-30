"""
Draws a us map with the UFO observations on it.
"""


import warnings
warnings.filterwarnings('ignore')

import random, math
import numpy as np
import scipy, scipy.stats

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
nicered = "#E6072A"
niceblu = "#424FA4"
nicegrn = "#6DC048"

import pandas as pd


#Reading all the data into pandas Data Frame.
df = pd.read_csv("ufo.csv", skiprows=1, names=["datetime", "city", "state", "country", "shape",
                                              "duration_sec", "duration_h", "comments", "posted",
                                              "latitude", "longitude"],
                                              low_memory=False)
#Getting US only Data Frame.
df_us = df[df["country"]=="us"].drop("country", 1)
df_us.dropna()
df_us[["latitude"]] = df_us[["latitude"]].apply(pd.to_numeric)

#Getting observations counted by states.
observ_counted = df_us.state.value_counts()

#Build the map:
m = Basemap(llcrnrlon=-119,llcrnrlat=22, # define map corners
            urcrnrlon=-64, urcrnrlat=49,
            projection='lcc', # lambert conformal conic project
            lat_1=33,lat_2=45,lon_0=-95,resolution='c')

#Draw the US:
m.drawcoastlines()
m.drawstates()
m.drawcountries()

#Draw the UFO ibservations
max_size=10
for i, city in df_us[:10000].iterrows():
    x, y = m(city.longitude, city.latitude)
    m.scatter(x,y,
              marker='o',color=niceblu, alpha=0.5)
plt.show()
