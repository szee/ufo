"""
Calculates correlation coefficient between population of the state and number of UFO observations in it.
"""


import pandas as pd
import csv
import numpy as np


with open("population.csv") as csv_popul:
    reader = csv.reader(csv_popul)
    population_dict = {row[0].lower():int(row[1]) for row in reader}

df = pd.read_csv("ufo.csv", skiprows=1, names=["datetime", "city", "state", "country", "shape",
                                              "duration_sec", "duration_h", "comments", "posted",
                                              "latitude", "longitude"], low_memory=False)
#Getting US only Data Frame.
df_us = df[df["country"]=="us"].drop("country", 1)
#Getting observations counted by states.
observ_counted = dict(df_us.state.value_counts())
#Preparing matrix for correlation coefficient calculation.
ob_pop = np.zeros((52,2))
i = 0
for key in observ_counted:
    ob_pop[i, 0] = observ_counted[key]
    ob_pop[i, 1] = population_dict[key]
    i += 1

print(np.corrcoef(ob_pop.T))
"""
Correlation coefficient is 0.91701094
"""
