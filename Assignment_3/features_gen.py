import pandas as pd
import numpy as np
import math
import pylab as pl
from sklearn.ensemble import RandomForestClassifier

def make_bins(df, feature, type_cut, quantiles = 0.5, bins = 1):
    valid_cuts = ['quantiles', 'bins']
    assert type_cut in valid_cuts

    bins = 'bins_{}'.format(feature)
    if type_cut == 'quantiles':
        df[bins] = pd.qcut(df[feature], quantiles, labels=False)
    elif type_cut == 'n':
        df[bins] = pd.cut(df[feature], bins, labels=False)
