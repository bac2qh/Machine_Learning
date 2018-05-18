import pandas as pd
import matplotlib.pyplot as plt


def explore(df):
    dic = {}
    summary = df.describe()
    features = list(df)[lead_var:]
    dic["summary"] = summary
    dic["features"] = features

    return dic

def explore_var(df,var,plot_type):
    dic_var = {}
    cols = [var, dep_var]
    var_mean = df[cols].groupby(var).mean()
    plot = var_mean.plot(kind=plot_type,use_index=False,figsize=(10,6))

    dic_var["distribution"] = var_mean
    dic_var["plot"] = plot

    return dic_var
