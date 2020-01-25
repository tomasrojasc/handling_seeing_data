# handling_seeing_data


## Description of the files

  * __``resampling_data.py``__: This script is used for creating dictionaries of resampled data from the original csv files located at ``original_data/`` folder.
  * __``creating_resampled_df_from_resampled_data.py``__: This script takes the files made by the previous one and merge everything into a big pandas dataframe containing all the resampled data. This is a preview of such dataframe:
  ```
      datetime	 paranal 	armazones 	date_key 	sampling_rate
    0 	2004-11-01 23:30:00 	0.820000 	NaN 	2004-11-01 	1
    1 	2004-11-01 23:31:00 	0.840000 	NaN 	2004-11-01 	1
    2 	2004-11-01 23:32:00 	0.800000 	NaN 	2004-11-01 	1
    3 	2004-11-01 23:33:00 	0.720000 	NaN 	2004-11-01 	1
    4 	2004-11-01 23:34:00 	0.710000 	NaN 	2004-11-01 	1
    ... 	... 	... 	... 	... 	...
    17 	2009-09-29 07:30:00 	1.136333 	NaN 	2009-09-28 	30
    18 	2009-09-29 08:00:00 	1.223667 	NaN 	2009-09-28 	30
    19 	2009-09-29 08:30:00 	1.402000 	NaN 	2009-09-28 	30
    20 	2009-09-29 09:00:00 	1.239333 	NaN 	2009-09-28 	30
    21 	2009-09-29 09:30:00 	1.388667 	NaN 	2009-09-28 	30
  ```
## Things to remember
  * Ask for the weather data
  * important dates such as ``2009-04-01``
## TODO
Still missing things to do:

  * Create a function that canrecieve a df and add a new column for the mean normalized data. This should be generic enough so one can pass filtered dataframes one at a time.
  * Create a function that compute the correlations for the non_mean_norm data and the raw_data. This correlations should be saved as a dictionary that can be consulted with the date_key and the sampling_rate, it must contain a dataframe with the actual data.
  * A dataframe tha has the maximum values for the correlation functions as well as the corresponding shift. This should be __one__ dataframe with those values, date_key and sampling_rate as keys.

Once all that is achieved we can move on to making an easy-to-use script wrapping everything. Then we can move on to the visualization.
