import os


venv = 'python3.7'
os.system(venv + ' ' + 'resampling_data.py')
os.system(venv + ' ' + 'adding_date_key_column_to_dicts.py')
os.system(venv + ' ' + 'adding_mean_norm_cols.py')
os.system(venv + ' ' + 'add_sampling_rate_col.py')
os.system(venv + ' ' + 'generate_time_series_df.py')
os.system(venv + ' ' + 'generate_cross_corr_dicts.py')
os.system(venv + ' ' + 'creating_corr_dict_final.py')
os.system(venv + ' ' + 'shifts_to_minutes.py')
os.system(venv + ' ' + 'creating_max_corr_df.py')
