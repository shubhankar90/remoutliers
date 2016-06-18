"""
@author: shubhankar.mitra
"""
import pandas as pd

def rem_outlier(ds,col,upperLimit,lowerLimit):
    #print(len(ds))
    #print((ds[col].mean()-ds[col].median())/ds[col].median())
    if  (ds[col].mean()-ds[col].median())/ds[col].median()>upperLimit:
        #print(ds[ds[col]==ds[col].max()])
        ds=ds[ds[col]!=ds[col].max()]
        return rem_outlier(ds,col)
    elif (ds[col].mean()-ds[col].median())/ds[col].median()<-lowerLimit:
        #print(ds[ds[col]==ds[col].min()])
        ds=ds[ds[col]!=ds[col].min()]
        return rem_outlier(ds,col)
    else:
        return(ds)