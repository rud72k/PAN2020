def carisegmen(xData,x):
    '''mencari interval pada xData dimana x berada. Nilai yang dihasilkan adalah batas kiri interval'''
    kiri = 0
    kanan = len(xData)- 1
    while True:
        if (kanan-kiri) <= 1:
            return kiri
        i =int((kiri + kanan)/2)
        if x < xData[i]: kanan = i
        else: kiri = i

def interpolasigaris(xData, yData, x0):
    '''menginterpolasi x berdasarkan xData'''
    x, y = xData, yData
    k = carisegmen(x, x0)
    y0 = y[k] + (x0-x[k])*(y[k+1] - y[k])/(x[k+1] - x[k])
    return(y0)
