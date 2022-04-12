#import numpy as np
import pandas as pd
import os
import glob

DIR_ROOT = os.getcwd()
DIR_DATA = os.path.join(DIR_ROOT,'data')
PATH_DATASET_TO = os.path.join(DIR_DATA, 'tocantins.csv')

def main():

    #reading data from files
    csv_files = glob.glob(os.path.join(DIR_DATA, "*.csv"))

    #creating new dataset
    dataset_tocantins = pd.DataFrame()

    for file in csv_files:
        
        df_ = pd.read_csv(file, sep=';')
        dataset_tocantins = pd.concat([dataset_tocantins, df_[df_['estado'] == 'TO']])

    dataset_tocantins.to_csv(PATH_DATASET_TO, sep=';')

if __name__ == "__main__":
    main()