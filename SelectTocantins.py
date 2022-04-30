import pandas as pd
import os
from glob import glob

DIR_ROOT = os.getcwd()
DIR_DATA = os.path.join(DIR_ROOT,'data')
PATH_DATASET_TO = os.path.join(DIR_DATA, 'tocantins.csv')

def select_tocantins_files():

    #reading data from files
    csv_filename_list = glob(os.path.join(DIR_DATA, "*.csv"))

    #creating new dataset
    dataframe_tocantins = pd.DataFrame()

    for csv_file in csv_filename_list:
        
        df_ = pd.read_csv(csv_file, sep=';')
        dataframe_tocantins = pd.concat([dataframe_tocantins, df_[df_['estado'] == 'TO']])
        os.remove(csv_file)

    dataframe_tocantins.to_csv(PATH_DATASET_TO, sep=';', index=False)