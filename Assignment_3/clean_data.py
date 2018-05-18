import pandas as pd

def nans(df):
    df_lng = pd.melt(df)
    null_variables = df_lng.value.isnull()
    return pd.crosstab(df_lng.variable, null_variables)

def fill(df,var,fill_method):
    if fill_method == "zero":
        df[var] = df[var].fillna(0)
    elif fill_method == "mean":
        df[var] = df[var].fillna(df[var].mean())
    elif fill_method == "drop":
        df[var] = df[var].dropna()
    elif fill_method == "pad" or fill_method == "ffill":
        df[var] = df[var].fillna(method=fill_method)
    else:
        raise ValueError('{method} not available'.format(method=fill_method))
    return df
