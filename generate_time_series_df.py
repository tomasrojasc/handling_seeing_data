import pandas as pd
import pickle
import os
from utils import *


interest_folder = './processed_data/resampled_data/'

files_dicts = os.listdir(interest_folder)

paths_2_dict = [interest_folder + i for i in files_dicts]
paths_2_dict.sort()


number_of_minutes = [int(paths_2_dict[i][32:-13]) for i in range(len(paths_2_dict))]


all_dfs = []

for i, path in enumerate(paths_2_dict):
    print('opening ' + path)
    with open(path, 'rb') as f:
        current_dict = pickle.load(f)
    f.close()
    current_df = make_df_from_dict(current_dict)
    all_dfs.append(current_df)

print('merging...')
time_series_df = pd.concat(all_dfs)

print('saving big df...')
with open('final_data/' + 'time_series_data.timeseries', 'wb') as f:
    pickle.dump(time_series_df, f)
f.close()

