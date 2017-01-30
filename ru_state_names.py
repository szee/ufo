"""
Adds russian translation for every state name to the file with data (ufo.csv).
"""


import pandas as pd
import csv


#Creating dictinary for mapping
with open("codes.csv") as csv_codes:
    reader = csv.reader(csv_codes)
    codes_dict = {row[1].lower():row[0] for row in reader}

#Reading all the data from "ufo.csv" into pandas Data Frame.
df = pd.read_csv("ufo.csv", skiprows=1, names=["datetime", "city", "state", "country", "shape",
                                              "duration_sec", "duration_h", "comments", "posted",
                                              "latitude", "longitude"], low_memory=False)

#Adding column with states' names translated
df["state_ru"] = df["state"].map(codes_dict)

#Getting the real first line from "ufo.csv" and adding column name for the russian states' names
with open("ufo.csv") as rdr:
    header = next(csv.reader(rdr))
header.append("state_ru")

#Creating a file with the added column
df.to_csv("ufo_ru.csv", header=header, index=False, encoding="utf-8")


#df_st_set = set(df.state)
#df_tr_set = set(codes_dict.keys())

#print(df_tr_set - df_st_set)
#print(df[~df.state.isin(codes_dict.keys())])
