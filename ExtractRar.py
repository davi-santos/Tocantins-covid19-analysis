import os
from patoolib import extract_archive #pip install patool

DIR_ROOT = '.'
DIR_DATA = 'data'
DATA_PATH = os.path.join(DIR_ROOT, DIR_DATA)
LIST_OF_FILENAMES_IN_DATA_DIRECTORY = os.listdir(DATA_PATH)

print(DATA_PATH)
print(LIST_OF_FILENAMES_IN_DATA_DIRECTORY)

def check_rar_data_directory():
    for filename in LIST_OF_FILENAMES_IN_DATA_DIRECTORY:
        if '.rar' in filename:
            return True
    return False

def extract_files_from_rar():
    
    if not check_rar_data_directory():
        print('Arquivo .rar não encontrado no Diretório "data"')
        return
    
    rar_filename = ''

    for filename in LIST_OF_FILENAMES_IN_DATA_DIRECTORY:
        if '.rar' in filename:
            rar_filename = os.path.join(DATA_PATH, filename)
            break

    print('... Extraindo arquivos compactados para o diretório data')
    extract_archive(rar_filename,  outdir=DATA_PATH)

    print('--------------------------')
    print('Arquivos extraídos com sucesso')
    print('... Apagando .rar')
    os.remove(rar_filename)