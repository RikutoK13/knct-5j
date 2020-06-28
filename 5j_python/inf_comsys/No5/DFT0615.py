import numpy as np
import matplotlib.pyplot as plt


def dft(x,N):
    X=np.zeros(N,dtype=complex)
    for k in range(？？？):
        re=？？？
        im=？？？
        for n in range(？？？):
            re+=x[n]*np.cos(？？？)
            im+=x[n]*np.sin(？？？)
            X[k]=complex(re,im)
            return X
N=128t = np.arange(0, N)C = np.sin(2*np.pi*t/N*10)C=dft(C,N)C=np.abs(C) **2plt.plot(t,C)plt.show()