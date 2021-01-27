import numpy as np
import matplotlib.pyplot as plt

def Lj1(x, k, x0):
    ''' data disimpan di x, nilai yang dihitung x0 '''
    lj = 1                    					# sebagai nilai awal. Karena involved perkalian, maka ini di set 1
    											# kalau operasinya penjumlahan, nilai awal diset 0
    for i in range(len(x)):								
        if i == k:								# membuang perkalian yang mempunyai indeks yang  k
            continue
        else:
            lj *= (x0 - x[i])/(x[k] - x[i]) 	# lalu mengalikan semua faktor yang dibutuhkan   (x - x_i) / (x_k - x_i)
    return(lj)

def lagrange1(x, y, x0):
    '''Interpolasi Lagrange dengan data input berupa matriks'''

    P = 0										# sebagai nilai awal. Karena involved pernjumlahan, maka ini di set 0
    											# kalau operasinya perkalian, nilai awal diset 1

    Lj = [Lj1(x, k, x0) for k in range(len(x))] # menyimpan semua nilai Lj  untuk j=0,1,2,...,n

    
    for k in range(len(x)):
        P = P + y[k]*Lj[k]						# lalu mengalikan semua nilainya

    return(P)