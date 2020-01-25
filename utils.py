from datetime import timedelta, datetime
from scipy.signal import correlate
import numpy as np
import pandas as pd
import os
import pickle
import matplotlib.dates as mdates
from numpy import polyfit

def grouper_UT(df, UTb, UTe):
    '''
    df: df to slice (must be sorted by date)
    UTb: begining UT time of interest
    UTe: end of UT time of interest (next day)

    return: a list of dfs with the slices
    '''
    n_days = (df.index[-1] - df.index[0]).days

    date_0 = df.index.date[0]
    date_f = date_0 + timedelta(days=1)

    date_0 = datetime.combine(date_0, UTb)
    date_f = datetime.combine(date_f, UTe)

    condition = (date_0 < df.index) & (df.index < date_f)
    conditions = [condition]
    conditions += [((date_0 + timedelta(days=i)) < df.index) & (
                df.index < (date_f + timedelta(days=i)))
                   for i in range(n_days)]

    UT_days = [df.loc[single_condition] for single_condition in conditions]


    return UT_days


def list2dict(list_dfs):
    """
    it takes a list of sliced dfs and turns it into a dict with
    the date as key
    :param list_dfs: a list of ut sampled dfs
    :return: a dict of ut sampled dfs
    """

    return {df.index[0].strftime('%Y-%m-%d'): df for df in list_dfs
            if len(df) != 0}


def resample_df(dict_df, T):

    """
    this function resamples a dict of df to the desired sampling rate
    and returns a dict identical but with the new sampling rate
    :param dict_df: dictionary of dfs to resample
    :param T: sampling rate as str (example: '5Min')
    :return: a dictionary of dataframes with the new sampling rate
    """
    return {date: dict_df[date].resample(T).mean()
            for date in dict_df}


def correlate_dfs(dict_df, T):
    """
    this function calculate the cross corr for a dict of dfs and returns
    a dict with the same days as keys but with dataframes corresponding
    to the shifts in minutes and corr
    :param dict_df: dictionarí of the utdf
    :param: T: time sampling rate dor the dict
    :return: dictionary with the correlations
    """

    corr_dict = {}
    for date in dict_df:
        s1 = dict_df[date].paranal
        s2 = dict_df[date].armazones
        corr = correlate(s1, s2, 'full')
        shift = np.arange(0, len(corr), 1)
        shift -= (len(s1) - 1) # put the two signals in phase
        shift *= T
        corr_dict[date] = pd.DataFrame({'shift': shift, 'corr': corr})

    return corr_dict


def get_polinomial_parameters(dict_df, degree):
    """
    This function gets a polynomial fit for a dict of utdfs
    :param dict_df: utdf dict
    :param degree: degree of the polynomial desired
    :return: dict of dicts with the parameters consulted with sub keys
    """

    parameters_dict = {}

    for date in dict_df:
        if len(dict_df[date].dropna()) != 0:
            df1 = dict_df[date].paranal.dropna()
            df2 = dict_df[date].armazones.dropna()
            index_1_0 = df1.index[0]
            index_2_0 = df2.index[0]
            p1 = polyfit((df1.index-index_1_0).total_seconds(), df1.values, degree)
            p2 = polyfit((df2.index-index_2_0).total_seconds(), df2.values, degree)
            sub_dict = {'paranal_parameters': p1,
                        'armazones_parameters': p2}
            parameters_dict[date] = sub_dict

    return parameters_dict




def get_resampled_data_merged_df(data_path):
    """
    creates a dataframe of all resampled data from a path
    :param data_path: folder where the data is
    :return: pandas df
    """
    print('getting resampled_raw_data')
    resampled_data_paths = os.listdir(data_path)

    resampled_data_dfs = []

    # for each name of file
    for resampling_rate in resampled_data_paths:
        # open it
        print('opening ' + data_path + resampling_rate)
        with open(data_path + resampling_rate, 'rb') as f:
            current_resampled_data = pickle.load(f)
        f.close()

        # see all the dates present in the current dict
        for date in current_resampled_data:

            df = current_resampled_data[date]

            new_df = pd.DataFrame({'date_key': date,
                                   'datetime': df.index,
                                   'sampling_rate': int(resampling_rate[:-13]),
                                   'paranal_raw': df.paranal.values,
                                   'armazones_raw': df.armazones.values
                                   })

            resampled_data_dfs.append(new_df)

    print('merging the data, this may take a while...')
    print('\n\n\n\n\n')
    # dataframe for the resampled data
    return pd.concat(resampled_data_dfs).sort_values(['sampling_rate', 'datetime'])







def get_mean_norm_data_merged_df(data_path):
    """
    creates a dataframe of all resampled data from a path
    :param data_path: folder where the data is
    :return: pandas df
    """
    print('getting mean_norm_data')
    mean_norma_paths = os.listdir(data_path)

    mean_norm_dfs = []

    # for each name of file
    for resampling_rate in mean_norma_paths:
        # open it
        print('opening ' + data_path + resampling_rate)
        with open(data_path + resampling_rate, 'rb') as f:
            current_mean_norm_data = pickle.load(f)
        f.close()

        # see all the dates present in the current dict
        for date in current_mean_norm_data:

            df = current_mean_norm_data[date]

            new_df = pd.DataFrame({'date_key': date,
                                   'datetime': df.index,
                                   'sampling_rate': resampling_rate[:-13],
                                   'paranal_mean_norm': df.paranal.values,
                                   'armazones_mean_norm': df.armazones.values
                                   })

            mean_norm_dfs.append(new_df)

    print('merging the data, this may take a while...')
    print('\n\n\n\n\n')
    # dataframe for the resampled data
    return pd.concat(mean_norm_dfs).sort_values('datetime').sort_values(['sampling_rate', 'datetime'])


def get_correlation_to_pd(data_path, what):
    """
    creates a dataframe of all correlations from path to folder
    :param data_path: folder where the data is
    :param what: mean or non_mean
    :return: pandas df
    """


    if what=='non_mean':
        slice_n = -15
    if what=='mean':
        slice_n = -12

    print('getting mean_norm_corr')
    # file names
    mean_norm_corr_paths = os.listdir(data_path)

    mean_norm_corr_dfs = []

    # for each name of file
    for resampling_rate in mean_norm_corr_paths:
        # open it
        print('opening ' + data_path + resampling_rate)
        with open(data_path + resampling_rate, 'rb') as f:
            current_mean_norm_corr = pickle.load(f)
        f.close()

        T = int(resampling_rate[:slice_n])
        # see all the dates present in the current dict
        for date in current_mean_norm_corr:
            df = current_mean_norm_corr[date]

            if np.all(np.isnan(np.array([df['corr'].values]).reshape(-1))):
                max_corr_actual = np.nan
                corr_shift_actual = np.nan
            else:
                max_corr_actual = np.nanmax(np.array([df['corr'].values]).reshape(-1))
                corr_shift_actual = [[df['shift'].values * T][np.nanargmax(max_corr_actual)]]


            new_df = pd.DataFrame({'date_key': date,
                                   'delay_in_min': [np.array([df['shift'].values * T]).reshape(-1)],
                                   'corr': [np.array([df['corr'].values]).reshape(-1)],
                                   'max_corr': max_corr_actual,
                                   'corresponding_shift': corr_shift_actual,
                                   'sampling_rate': resampling_rate[:slice_n],
                                   })

            mean_norm_corr_dfs.append(new_df)

    print('merging the data, this may take a while...')
    print('\n\n\n\n\n')
    # dataframe for the resampled data
    return pd.concat(mean_norm_corr_dfs).sort_values(['sampling_rate', 'date_key'])



def add_date_key_to_dfs_of_dictionary(dict_of_dfs):
    """
    this function takes a dictionary that contains many resampled days
    and puts a date_key into them to retun a whole df
    :param dict_of_dfs: a dictionary of dfs (have to open bin first)
    :return: a big df with all the days and keys
    """
    keys = [i for i in dict_of_dfs]
    for key in keys:
        dict_of_dfs[key].loc[:, 'date_key'] = dict_of_dfs[key].index[0].strftime('%Y-%m-%d')
        dict_of_dfs[key].reset_index(level=0, inplace=True)

    list4concat = [dict_of_dfs[key] for key in keys]

    return pd.concat(list4concat).sort_values('datetime')