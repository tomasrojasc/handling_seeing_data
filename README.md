# handling_seeing_data


## Description of the files
  * __``utils.py``__: This script contains all the functions that the other scripts may need.
  * __``resampling_data.py``__: This script is used for creating dictionaries of resampled data from the original csv files located at ``original_data/`` folder.
  * __``adding_date_key_column_to_dicts.py``__: This script takes the files made by the previous one and overwrite each dict but each df now has the ``"date_key"`` column.
  * __``adding_mean_norm_cols.py``__: This file takes all the resampled dicts dataframes and puts a mean norm column in each one, one for location. Then it overwrites the data.
  * __``add_sampling_rate_col.py``__: This script takes all the resampling dict dataframes and uses them to add the sampling rate.
  * __``generate_time_series_df.py``__: This script creates a big dataframe with all the time series data, normalized and not normalized and saves it into a dataframe as binary file.
  * __``generate_cross_corr_dicts.py``__: This file make a bunch of dicts with the correlations. One dict per ``sampling_rate``
  * __``creating_corr_dict_final.py``__: This file takes all the individual dicts for the sampling rates and creates a dictionary with the first key being the ``sampling_rate`` and the second being the ``date_key``
## Workflow

_Before reading: you can just run the ``main.py`` file and it will execute all the scripts in the order below_

Even though there are scripts that does not matter when they are executed, it is suggested to run the files in this order:
  * ``resampling_data.py``
  * ``adding_date_key_column_to_dicts.py``
  * ``adding_mean_norm_cols.py``
  * ``add_sampling_rate_col.py``
  * ``generate_time_series_df.py``

At this point you should have a pandas df with all the information of time series at different sampling rates.

The following steps are for getting the correlations just right from the previous data:

  * ``generate_cross_corr_dicts.py``
  * ``creating_corr_dict_final.py``

With this, the dictionary with the correlations is ready. Now we need a maximum correlation dataframe which is obtained by executing the file:

  * ``creating_max_corr_df.py``

Now you should have a dictionary with the corresponding correlations. The first key is the ``sampling_rate`` and the second one is the ``date_key``





## Things to remember
  * Ask for the weather data
  * important dates such as ``2009-04-01``
