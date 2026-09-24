"""Forecasting metrics."""
import numpy as np
def mae(y_true,y_pred): return float(np.mean(np.abs(np.asarray(y_true)-np.asarray(y_pred))))
def rmse(y_true,y_pred): return float(np.sqrt(np.mean((np.asarray(y_true)-np.asarray(y_pred))**2)))
def smape(y_true,y_pred):
    y_true,y_pred=np.asarray(y_true),np.asarray(y_pred)
    d=np.abs(y_true)+np.abs(y_pred)
    return float(100*np.mean(2*np.abs(y_pred-y_true)/np.where(d==0,1,d)))
