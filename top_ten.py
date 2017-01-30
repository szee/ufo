"""
Gets top 10 states by UFO observations.
"""


import pandas as pd


#Reading all the data into pandas Data Frame.
df = pd.read_csv("ufo.csv", skiprows=1, names=["datetime", "city", "state", "country", "shape",
                                              "duration_sec", "duration_h", "comments", "posted",
                                              "latitude", "longitude"], low_memory=False)
#Getting US only Data Frame.
df_us = df[df["country"]=="us"].drop("country", 1)
#Getting observations counted by states.
observ_counted = df_us.state.value_counts()
#Printing top 10 states.
print(observ_counted[:10])


print(df_us.longitude, df_us.latitude)
