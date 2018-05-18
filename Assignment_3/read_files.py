import os
import pandas as pd

def read(file_name):
    path = 'data/'+ file_name
    ext = os.path.splitext(path)[-1].lower()
    # for csv files
    if ext == ".csv":
        df = pd.read_csv(path)
    # for xls files
    elif ext == ".xls":
        df = pd.read_excel(path)
    elif ext == ".xlsx":
        df = pd.read_excel(path)
    else:
        raise ValueError('cannot read the {file} in pandas'.format(file = path))
    return df
