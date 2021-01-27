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

##############################################################

## Contoh 1 

x = np.linspace(0,2.1,21)			# sebagai input data x
y = x**2 - x + 1					# sebagai input data y

ans= lagrange1(x,y,0.5)				# menginterpolasi f(0.5)


##############################################################

## Contoh 2 
## Diberikan titik data (0,4),(2,1),(3,-4),(6,8)
## akan dibuat interpolasi untuk semua titik di interval [0,6]

A = np.array([[0,4],[2,1],[3,-4],[6,8]])
x = A[:,0]
y = A[:,1]

t =  np.linspace(0,6,1000)			# inisiasi titik-titik yang akan diinterpolasi
#z = t*0								# inisiasi nilai z = f(t). Agar memiliki dimensi yang sama 
									# dengan t, maka dibuat z = t*0  
									# bisa juga dengan menginisiasi dengan cara z = np.zeros(1000)

z = [lagrange1(x,y,t[i]) for i in range(len(t))]			# melakukan interpolasi untuk seluruh nilai di vektor t



plt.plot(x,y,'ro') 		# plot nilai sampel. argumen 'ro' artinya red, circle  => lihat di gambar
plt.plot(t,z)			# memplot hasil interpolasi pada gambar yang sama dengan plot sebelumnya
plt.show()


#############################################################

x = [-3,-2,-1,0,1,2,3,4]
y = [ 2, 3, 4,5,4,3,2,1]

t = np.linspace(-3.5,4.5,1000)
ft = [lagrange1(x,y,t[i]) for i in range(1000)]

# plt.plot(x,y,'ro')        # plot nilai sampel. argumen 'ro' artinya red, circle  => lihat di gambar
# # plt.plot(x,y,'-b')
# plt.plot(t,ft)         # memplot hasil interpolasi pada gambar yang sama dengan plot sebelumnya

# plt.show()