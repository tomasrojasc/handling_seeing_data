from utils import shift_to_actual_minutes
import pickle



path = 'final_data/corr_dict.correlations'

with open(path, 'rb') as f:
    corr_dict = pickle.load(f)
f.close()

for sampling_rate in corr_dict:
    print('computing sampling rate to min for: '+str(sampling_rate)+' minutes...')
    corr_dict[sampling_rate] = shift_to_actual_minutes(corr_dict[sampling_rate], sampling_rate)

print('overwriting...')
with open(path, 'wb') as f:
    pickle.dump(corr_dict, f)
f.close()
