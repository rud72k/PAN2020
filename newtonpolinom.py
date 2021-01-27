import numpy as np

def interpolasiNewtonPolinom(a,x,x0):
    '''Menghitung P(x) dengan a adalah koefisien polinom 
    x adalah data dan x0 adalah nilai yang akan diinterpolasi'''
    
    px = a[-1]
    for k in range(1,len(x)):
        px = a[-k] + (x0-x[-k])*px
    return(px)

def koefisienNewtonPolinom(x,y):
    '''x dan y adalah data yang akan diinterpolasi menjadi P(x)=y
    output fungsi ini adalah vektor berisi koefisien P'''
    m = len(x)
    a = y.copy()
    for k in range(1,len(x)):
        a[k:m] = (a[k:m] - a[k-1])/(x[k:m] - x[k-1])
    return(a)
