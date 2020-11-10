import numpy as np
import matplotlib.pyplot as plt
import time


def dft(x, N):
    X = np.zeros(N, dtype=complex)
    for k in range(N-1):
        re = np.cos(2 * np.pi / N)
        im = np.sin(2 * np.pi / N)
        for n in range(k):
            re += x[n] * np.cos(2 * np.pi * n * k / N)
            im += x[n] * np.sin(2 * np.pi * n * k / N)
        X[k] = complex(re, im)
    return X


N = 128
t = np.arange(0, N)
C = np.sin(2 * np.pi * t / N * 10)

C = dft(C, N)
C = np.abs(C) ** 2

plt.plot(t, C)
plt.show()
