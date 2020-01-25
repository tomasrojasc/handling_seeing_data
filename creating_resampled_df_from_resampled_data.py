import pandas as pd
import pickle
from utils import add_date_key_to_dfs_of_dictionary
import os


interest_folder = './processed_data/resampled_data/'

files_dicts = os.listdir(interest_folder)

paths_2_dict = [interest_folder + i for i in files_dicts]
paths_2_dict.sort()


number_of_minutes = [int(paths_2_dict[i][32:-13]) for i in range(len(paths_2_dict))]


all_dfs = []

for i, path in enumerate(paths_2_dict):
    print('making df for ' + path)
    with open(path, 'rb') as f:
        current_dict = pickle.load(f)
    f.close()

    current_df = add_date_key_to_dfs_of_dictionary(current_dict)
    current_df.loc[:, ('sampling_rate')] = number_of_minutes[i]
    all_dfs.append(current_df)

print('merging')
big_df = pd.concat(all_dfs).sort_values(['sampling_rate', 'datetime'])

print('saving')
with open('processed_data/resampled_data_dfs/resampled_data.dataframe', 'wb') as f:
    pickle.dump(big_df, f)
f.close()