import os
from patoolib import extract_archive

DIR_ROOT = '.'
DIR_DATA = 'data'
DATA_PATH = os.path.join(DIR_ROOT, DIR_DATA)

files_in_datapath = os.listdir(DATA_PATH)
zip_filename = ''

for f in files_in_datapath:
    if '.rar' in f:
        zip_filename = os.path.join(DATA_PATH, f)
        break

print('... Extracting data from .rar file')
extract_archive(zip_filename,  outdir=DATA_PATH)

#print('... Deleting rar file')
#os.remove(zip_filename)
