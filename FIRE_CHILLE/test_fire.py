import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
#import plotly_express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import scale

#def make_df(station_list):
    # Takes in the list and return a pandas dataframe, with Dates and Years as
    # separate columns
    
    #df_temp = pd.DataFrame(station_list, index=None, columns=['date', 'station', 'value'])
    # Good Groupby Tut -> https://realpython.com/pandas-groupby/
    #df_temp = df_temp.groupby("station", sort=False, as_index=False)
    
    #return df_temp

df = pd.read_csv('climate_data.csv')

df_copy = df.copy()

station_names = df['station'].unique()

#df_station = df_copy.groupby(df['station'])

#print(station_names)
#print(df_station.head())

st1 = []
st2 = []
st3 =[]
st4 =[]
st5 =[]
st6 = []
st7 = []
st8 = []
st9 = []
st10 = []
st11 = []
st12 = []
st13 = []
st14 = []
st15 = []
st16 = []

for station in station_names:
    print(station)
    
    if station == 'GHCND:CI000085469':
        print(df_copy[ 'station' == 'GHCND:CI000085469' ]['values'])      
    else:
       None
    # elif dat.month == 4:
    #     val = df_copy.loc[t]['Algae Con']
    #     time_val = [time_s, val]
    #     april.append(time_val)
    
    # elif dat.month == 5:
    #     val = df_copy.loc[t]['Algae Con']
    #     time_val = [time_s, val]
    #     may.append(time_val)

    # elif dat.month == 6:
    #     val = df_copy.loc[t]['Algae Con']
    #     time_val = [time_s, val]
    #     june.append(time_val)
    
    # elif dat.month == 7:
    #     val = df_copy.loc[t]['Algae Con']
    #     time_val = [time_s, val]
    #     july.append(time_val)
    
    # elif dat.month == 8:
    #     val = df_copy.loc[t]['Algae Con']
    #     time_val = [time_s, val]
    #     august.append(time_val)

    # elif dat.month == 9:
    #     val = df_copy.loc[t]['Algae Con']
    #     time_val = [time_s, val]
    #     september.append(time_val)
    
    # elif dat.month == 10:
    #     val = df_copy.loc[t]['Algae Con']
    #     time_val = [time_s, val]
    #     october.append(time_val)