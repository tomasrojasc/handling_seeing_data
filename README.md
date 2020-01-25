# handling_seeing_data


## Description of the files
  * __``utils.py``__: This script contains all the functions that the other scripts may need.
  * __``resampling_data.py``__: This script is used for creating dictionaries of resampled data from the original csv files located at ``original_data/`` folder.
  * __``adding_date_key_column_to_dicts.py``__: This script takes the files made by the previous one and overwrite each dict but each df now has the ``"date_key"`` column.
  * __``adding_mean_norm_cols.py``__: This file takes all the resampled dicts dataframes and puts a mean norm column in each one, one for location. Then it overwrites the data.
  * __``add_sampling_rate_col.py``__: This script takes all the resampling dict dataframes and uses them to add the sampling rate.


## Workflow

Even though there are scripts that does not matter when they are executed, it is suggested to run the files in this order:
  * ``resampling_data.py``
  * ``adding_date_key_column_to_dicts.py``
  * ``adding_mean_norm_cols.py``
  * ``add_sampling_rate_col.py``





## Things to remember
  * Ask for the weather data
  * important dates such as ``2009-04-01``
## TODO
Still missing things to do:


  * Create a function that compute the correlations for the non_mean_norm data and the raw_data. This correlations should be saved as a dictionary that can be consulted with the date_key and the sampling_rate, it must contain a dataframe with the actual data.
  * A dataframe tha has the maximum values for the correlation functions as well as the corresponding shift. This should be __one__ dataframe with those values, date_key and sampling_rate as keys.

Once all that is achieved we can move on to making an easy-to-use script wrapping everything. Then we can move on to the visualization.
