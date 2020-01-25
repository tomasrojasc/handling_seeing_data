import pandas as pd
from utils import *
from datetime import time
import pickle

"""
This code is for opening the plane csv files and saving a binary file
with a dict that has ut time days as keys and dfs as elements, then
it resamples the data
"""

# opening the data as dfs
print('opening data...')
paranal = pd.read_csv('./original_data/paranal.csv')
armazones = pd.read_csv('./original_data/armazones.csv')

# setting the names of the columns
paranal.columns = ['datetime', 'paranal']
armazones.columns = ['datetime', 'armazones']

# making the datetime column an actual datetime obj
paranal['datetime'] = pd.to_datetime(paranal['datetime'])
armazones['datetime'] = pd.to_datetime(armazones['datetime'])

# setting dates as index
paranal.set_index('datetime', inplace=True)
armazones.set_index('datetime', inplace=True)

# sorting by datetime
paranal.sort_index(inplace=True)
armazones.sort_index(inplace=True)

# big df with two sites
seeing_measurements = pd.concat([paranal, armazones], axis=1)


# UT interval to use
UT_interval = time(22, 0, 0), time(11, 0, 0)

# separating UT days
print('slicing...')
seeing_measurements_list = grouper_UT(seeing_measurements, *UT_interval)

# making the data to a dict
seeing_measurements_dict = list2dict(seeing_measurements_list)

# saving as a binary file
print('saving the file...')
with open('./processed_data/dicts_of_utdf.pickle', 'wb') as f:
    pickle.dump(seeing_measurements_dict, f)
f.close()
print('done')



# opening raw data
with open('./processed_data/dicts_of_utdf.pickle', 'rb') as f:
    data = pickle.load(f)
f.close()

# creating minutes intervals 1 min to 30 min
minutes = [str(i)+'Min' for i in range(1, 30+1)]

# creating all resampled binary files
for minute in minutes:
    print('computing resampling each '+minute[:-3]+' minutes...')
    current_resamping = resample_df(data, minute)
    with open('./processed_data/resampled_data/'+minute+'.resampled', 'wb') as f:
        pickle.dump(current_resamping, f)
    f.close()
