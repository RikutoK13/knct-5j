import numpy as np
import matplotlib.pyplot as plt
from random import randint

def main():
    signal = [randint(0, 1) for i in range(1024)]
    plt.title('Single NRZ')
    sngl_nrz = single_nrz(signal)
    fftplot(sngl_nrz, "Single NRZ")
    plt.show()

    plt.title('Multi NRZ')
    mult_nrz = multi_nrz(signal)
    fftplot(mult_nrz, "Multi NRZ")
    plt.show()

    plt.title('Single RZ')
    sngl_rz = single_rz(signal)
    fftplot(sngl_rz, "Single RZ")
    plt.show()

    plt.title('Multi RZ')
    mult_rz = multi_rz(signal)
    fftplot(mult_rz, "Multi RZ")
    plt.show()

    plt.title('Bipolar')
    biplr = ami(signal)
    fftplot(biplr, "Bipolar")
    plt.show()

    plt.title('Manchester Derby')
    mncstr = manmethod(signal)
    fftplot(mncstr, "Manchester derby")
    plt.show()

def single_nrz(signal):
    palse = [i * (-1)for i in signal]

    return np.array(palse)

def multi_nrz(signal):
    palse = [0 if i % 2 == 0 else 1 for i in signal]

    return np.array(palse)

def single_rz(signal):
    palse = []

    for i in signal:
        palse.append(0)
        palse.append(i * -1)
        palse.append(i * -1)
        palse.append(0)

    return np.array(palse)

def multi_rz(signal):
    palse = []
    for i in signal:
        palse.append(0)
        if i % 2 == 0:
            palse.append(1)
            palse.append(1)
        else:
            palse.append(-1)
            palse.append(-1)
            palse.append(0)

        return np.array(palse)
    
def ami(signal):
    palse = []

    flag = False
    for i in signal:
        palse.append(0)
    if i % 2 == 0:
        if flag:
            palse.append(-1)
            palse.append(-1)
            flag = False
        else:
            palse.append(1)
            palse.append(1)
            flag = True
    else:
        palse.append(0)
        palse.append(0)
        palse.append(0)

    return np.array(palse)

def manmethod(signal):
    palse = []

    for i in signal:
        if i % 2 == 0:
            palse.append(0)
            palse.append(1)
        else:
            palse.append(1)
            palse.append(0)
            return np.array(palse)

def fftplot(signal,name):
    t = np.arange(0,len(signal))
    F = np.fft.fft(signal)
    plt.plot(t,np.abs(F) ** 2, label=name)




if __name__ == "__main__":
    main()
