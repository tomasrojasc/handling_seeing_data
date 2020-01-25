from utils import *



interest_folder = 'processed_data/correlations/'

files_dicts = os.listdir(interest_folder)

paths_2_dict = [interest_folder + i for i in files_dicts]
paths_2_dict.sort()


number_of_minutes = [int(files_dicts[i][:-13]) for i in range(len(paths_2_dict))]


correlations_dict_final = {}

for i, path in enumerate(paths_2_dict):
    print('reading '+path+'...')
    with open(path, 'rb') as f:
        current_dict = pickle.load(f)
    f.close()
    correlations_dict_final[number_of_minutes[i]] = current_dict

with open('./final_data/corr_dict.correlations', 'wb') as f:
    pickle.dump(correlations_dict_final, f)
f.close()