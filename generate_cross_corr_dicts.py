import pandas as pd
import numpy as np
from utils import *
import os


interest_folder = './processed_data/resampled_data/'

files_dicts = os.listdir(interest_folder)

paths_2_dict = [interest_folder + i for i in files_dicts]
paths_2_dict.sort()


number_of_minutes = [paths_2_dict[i][32:-13] for i in range(len(paths_2_dict))]


path2save = 'processed_data/correlations/'


for i, path in enumerate(paths_2_dict):

    print('making correlations for ' + path)
    with open(path, 'rb') as f:
        current_dict = pickle.load(f)
    f.close()
    curren_corr_dict = correlate_a_dict(current_dict)
    name_2_save = number_of_minutes[i] + '.correlations'
    with open(path2save + name_2_save, 'wb') as f:
        pickle.dump(curren_corr_dict, f)
    f.close()







