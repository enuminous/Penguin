import numpy as np
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score, average_precision_score, accuracy_score

def binary_metrics(y,p):
    y=np.asarray(y,dtype=int)
    p=np.clip(np.asarray(p,dtype=float),1e-9,1-1e-9)
    out={
        "brier":float(brier_score_loss(y,p)),
        "log_loss":float(log_loss(y,np.c_[1-p,p],labels=[0,1])),
        "accuracy_0.5":float(accuracy_score(y,(p>=0.5).astype(int))),
    }
    if len(np.unique(y))>1:
        out["roc_auc"]=float(roc_auc_score(y,p))
        out["average_precision"]=float(average_precision_score(y,p))
    else:
        out["roc_auc"]=None
        out["average_precision"]=None
    return out

def noise_strata(y,p,noise_score):
    noise_score=np.asarray(noise_score,dtype=float)
    qs=np.quantile(noise_score,[0.33,0.66])
    masks={
        "low_noise":noise_score<=qs[0],
        "mid_noise":(noise_score>qs[0])&(noise_score<=qs[1]),
        "high_noise":noise_score>qs[1],
    }
    out={}
    for name,mask in masks.items():
        if mask.any():
            out[name]=binary_metrics(np.asarray(y)[mask],np.asarray(p)[mask])
    return out
