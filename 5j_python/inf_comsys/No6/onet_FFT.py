# 128, 256, 1024, 2048, 4096でサンプリング
# 細かくないけど、同時比較バージョン

import numpy as np
import matplotlib.pyplot as plt
import time

N = [128, 256, 1024, 2048, 4096]

def main():
    for n in range(len(N)):
        data_fft = func_fft(N[n])
        if n < len(N):
            plt.subplots_adjust(wspace=0.8, hspace=0.8)
            plt.subplot(2, 3, n+1)
            plt.plot(data_fft[0], data_fft[1])
        print('サンプリング周期:{} 実行時間{}'.format(N[n], data_fft[2]))
    plt.show()

def func_fft(samp):
    bgn_time = time.perf_counter()
    t = np.arange(0, samp)
    c = np.sin(2 * np.pi * t / samp)
    f = np.fft.fft(c)
    f = np.abs(f) ** 2
    end_time = time.perf_counter()

    return t, f, end_time-bgn_time

if __name__ == '__main__':
    main()
