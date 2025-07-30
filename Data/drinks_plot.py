import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
import pandas as pd
from IPython.display import display
from datetime import datetime, date, timedelta, time
import matplotlib.dates as mdates

# loadpath = "/Users/emmaruthwalsh/Documents/Summer2025-Research/Python/flan2_weights/"
loadpath = "/Users/emmaruthwalsh/Documents/Summer2025-Research/Python/flan1_weights/"

# FLAN1
known_tags = [1111110209209, 1111110252252, 1111111151150,
              1111111134135, 196471892, 19647186244, 19645782, 19644148217]

# ISSUE = NO 19645674 WEIGHTS FOR 16/07
# FLAN 2
# known_tags = [19645674, 19647181251, 1964711262, 11111114041,
# 1111110190190, 1111110192192, 1111111248249, 11111116362]
known_tags = [str(tag) for tag in known_tags]

# data_date=date(2025,7,20)

# concatenate
start_date = date(2025, 7, 17)
# marker_times=[datetime(2025,7,17,12,0,0), datetime(2025,7,18,12,0,0)]#add important dates here to add vertical lines on last plot
# last_date=date.today() #OR TYPE DESIRED DATE ON NEXT LINE AND UNCOMMENT IT
last_date = date(2025, 7, 30)
datetag = str(last_date)
d = last_date-start_date
days_to_plot = d.days
data_coll_events = pd.read_csv(loadpath + str(start_date) + "_events.csv")

for j in range(days_to_plot):
    day = start_date+timedelta(days=j+1)
    data = pd.read_csv(loadpath + str(day) + "_events.csv")
    frames = [data_coll_events, data]
    data_coll_events = pd.concat(frames)

df = data_coll_events
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Animal'] = df['Animal'].astype(str)
df['Drinks1'] = df['Drinks1'].astype(int)
df['Drinks2'] = df['Drinks2'].astype(int)
df['Date'] = df['Start_Time'].dt.date
# animal rfids = strings, drinks = integers to sum later, extracts date from start_time

df = df[df['Animal'].isin(known_tags)]
#  include only data from known_tags

new_df = df.groupby(['Date', 'Animal'])[
    'Drinks1'].sum().unstack(fill_value=0)

# groups by day and animal, sums drinks1 for each day+animal pair
# then unstack function moves data from rows to columns - each animal has column
# to form new dataframe
# fill_value = 0 just refers to entering 0 when no drinks taken over blank space - needed for no errors

print(new_df)
# sanity check

new_df_2 = df.groupby(['Date', 'Animal'])[
    'Drinks2'].sum().unstack(fill_value=0)
# same for drinks2

plt.figure(figsize=(16, 6))
# plotting

'''
for tag in new_df.columns:
    if (new_df[tag] < 8000).all():
        plt.plot(new_df.index, new_df[tag],
                 marker='o', label='Drinks 1: ' + tag)

for tag in new_df_2.columns:
    if (new_df_2[tag] < 8000).all():
        plt.plot(new_df_2.index, new_df_2[tag],
                 marker='o', label='Drinks 2: ' + tag)

# only plots drink sums less than 8000

'''

for tag in new_df.columns:
    plt.plot(new_df.index, new_df[tag], marker='o',
             label='Drinks 1: 'f"{tag}")
for tag in new_df_2.columns:
    plt.plot(new_df_2.index, new_df_2[tag],
             marker='o', label='Drinks 2: 'f"{tag}")
  
# plots new_df index = rows = dates on x-axis, against new_df tags = animals on y-axis

plt.title("FLAN1 : Total Drinks per Animal per Day")
plt.xlabel("Time")
plt.ylabel("Drinks")
plt.xticks(rotation=45)
plt.legend(title="RFIDs", loc='upper left')
plt.tight_layout()
plt.grid(True)



# REPEATED CODE FOR FLAN 2

loadpath = "/Users/emmaruthwalsh/Documents/Summer2025-Research/Python/flan2_weights/"
# loadpath = "/Users/emmaruthwalsh/Documents/Summer2025-Research/Python/flan1_weights/"

# FLAN1
# known_tags = [1111110209209, 1111110252252, 1111111151150,
# 1111111134135, 196471892, 19647186244, 19645782, 19644148217]

# ISSUE = NO 19645674 WEIGHTS FOR 16/07
# FLAN 2
known_tags = [19645674, 19647181251, 1964711262, 11111114041,
              1111110190190, 1111110192192, 11111116362, 1111111248249]
# 1111110192192, 11111116362, 1111111248249
known_tags = [str(tag) for tag in known_tags]

# data_date=date(2025,7,20)

# concatenate
start_date = date(2025, 7, 17)
# marker_times=[datetime(2025,7,17,12,0,0), datetime(2025,7,18,12,0,0)]#add important dates here to add vertical lines on last plot
# last_date=date.today() #OR TYPE DESIRED DATE ON NEXT LINE AND UNCOMMENT IT
last_date = date(2025, 7, 30)
datetag = str(last_date)
d = last_date-start_date
days_to_plot = d.days
data_coll_events = pd.read_csv(loadpath + str(start_date) + "_events.csv")

for j in range(days_to_plot):
    day = start_date+timedelta(days=j+1)
    data = pd.read_csv(loadpath + str(day) + "_events.csv")
    frames = [data_coll_events, data]
    data_coll_events = pd.concat(frames)

df = data_coll_events
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Animal'] = df['Animal'].astype(str)
df['Drinks1'] = df['Drinks1'].astype(int)
df['Drinks2'] = df['Drinks2'].astype(int)
df['Date'] = df['Start_Time'].dt.date

df = df[df['Animal'].isin(known_tags)]

new_df = df.groupby(['Date', 'Animal'])[
    'Drinks1'].sum().unstack(fill_value=0)
new_df_2 = df.groupby(['Date', 'Animal'])[
    'Drinks2'].sum().unstack(fill_value=0)

plt.figure(figsize=(16, 6))

'''
for tag in new_df.columns:
    if (new_df[tag] < 8000).all():
        plt.plot(new_df.index, new_df[tag],
                 marker='o', color='red', label='Drinks 1: ' + tag)

for tag in new_df_2.columns:
    if (new_df_2[tag] < 8000).all():
        plt.plot(new_df_2.index, new_df_2[tag],
                 marker='o', color='blue', label='Drinks 2: ' + tag)
'''

for tag in new_df.columns:
    plt.plot(new_df.index, new_df[tag], marker='o',
             label='Drinks 1: 'f"{tag}")
for tag in new_df_2.columns:
    plt.plot(new_df_2.index, new_df_2[tag],
             marker='o', label='Drinks 2: 'f"{tag}")


plt.title("FLAN2 : Total Drinks per Animal per Day")
plt.xlabel("Time")
plt.ylabel("Drinks")
plt.xticks(rotation=45)
plt.legend(title="RFIDs", loc='upper left')
plt.tight_layout()
plt.grid(True)


plt.show()
