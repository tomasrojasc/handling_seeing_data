from utils import *
import pandas as pd
import pickle

print('opening data...')
with open('final_data/corr_dict.correlations', 'rb') as f:
    corr_dict = pickle.load(f)
f.close()

dfs_4_concat = []
for sampling_rate in corr_dict:
    print('creating max_corr_df for sampling rate = '+str(sampling_rate)+'minutes...')
    current_max_corr_df = get_max_corr_from_dict(corr_dict[sampling_rate])
    current_max_corr_df.loc[:, ('sampling_rate')] = sampling_rate
    dfs_4_concat.append(current_max_corr_df)

print('merging  everything...')
big_max_corr_df = pd.concat(dfs_4_concat)

big_max_corr_df.sort_values(['sampling_rate', 'date_key'], inplace=True)



print('now saving...')
with open('final_data/max_corr_df.correlations', 'wb') as f:
    pickle.dump(big_max_corr_df, f)
f.close()
