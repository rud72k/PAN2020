# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 06:20:33 2019

@author: Dad
"""

import numpy as np
from pandas import DataFrame

def F(x):
  y = x - np.sin(10*x)
  return(y)

def bisection(low,high,f,error):
  A = np.array([[low,(low+high)/2,high]])
  N = 0
  NMAX = np.ceil((np.log(abs(high-low)) - np.log(error))/np.log(2))
  print('Maksimum iterasi =',NMAX)
  print('Silakan tunggu ...')
  # langkah ini mengecek apakah ujung interval keduanya positif
  elif f(low)*f(high) > 0:
    print('Metode biseksi gagal, coba inteval lain.') 
    break

  while N < NMAX+1:
    mid = (low+high)/2
    # langkah ini hanya mengecek apakah ujung interval adalah akar
    if f(low)*f(high)*f(mid) == 0:  
      print('cek lagi siapa yang akar, low, mid, atau high')
      break
    # berikut adalah inti metode biseksi
    elif f(low)*f(mid) < 0:
      low = low
      high = mid
      mid = (low+high)/2
    elif f(mid)*f(high) < 0:
      high = high
      low = mid
      mid = (low+high)/2
    N += 1
    A = np.append(A, [[low,mid,high]],axis=0)
    if high-low < error:
        print("banyak iterasi dibutuhkan = ",N)
        print("akar =",mid)
        print("eror hingga =",error)
        break
  else:
    print('Metode biseksi gagal.')
  return(mid,A)
  
akar, tabel = bisection(-np.pi/2+0.1,np.pi/2,F,1e-7)

tabel = DataFrame(tabel,columns=['low','mid','high'])
print('  ')
print(tabel)