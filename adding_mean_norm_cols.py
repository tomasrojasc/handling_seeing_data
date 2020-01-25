import pandas as pd
import pickle
from utils import *
import os


interest_folder = './processed_data/resampled_data/'

files_dicts = os.listdir(interest_folder)

paths_2_dict = [interest_folder + i for i in files_dicts]
paths_2_dict.sort()


number_of_minutes = [int(paths_2_dict[i][32:-13]) for i in range(len(paths_2_dict))]


n_path = str(len(paths_2_dict))

all_dfs = []

for i, path in enumerate(paths_2_dict):
    with open(path, 'rb') as f:
        current_dict = pickle.load(f)
    f.close()
    print('\n\n\n')
    print('mean normalizing for file: ' + path + '    ' + '(' + str(i) + '/' + str(n_path) + ')')

    current_dict = mean_normalize(current_dict)

    print('overwriting...')
    with open(path, 'wb') as f:
        pickle.dump(current_dict, f)
    f.close()
