# *SK(new) means waveforms that have been changed in frequency

import numpy as np
import matplotlib.pyplot as plt


N = 128
t = np.arange(0, N, 1)

signal = [0, 1, 0, 1, 0, 1, 0, 1, 0]

def main():
    f = 4
    psk = p_shift_key(f)
    m_psk = p_shift_key(f)

    plt.subplot(2, 3, 1)
    plt.title("PSK")
    plt.plot(range(len(psk)), psk)
    plt.subplot(2, 3, 2)
    plt.title("PSK(modulated)")
    plt.plot(range(len(m_psk)), m_psk)
    plt.subplot(2, 3, 3)
    plt.title("PSK")
    plt.plot(range(len(psk)), psk)
    plt.subplots_adjust(wspace=0.4, hspace=0.6)

    f = int(input())  # 周波数を変える
    psk = p_shift_key(f)
    m_psk = p_shift_key(f)

    plt.subplot(2, 3, 4)
    plt.title("PSK(new)")
    plt.plot(range(len(psk)), psk)
    plt.subplot(2, 3, 5)
    plt.title("PSK(modulated)")
    plt.plot(range(len(m_psk)), m_psk)
    plt.subplot(2, 3, 6)
    plt.title("PSK(new)")
    plt.plot(range(len(psk)), psk)
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    plt.show()

def a_shift_key(fc):
    ask = []
    wave0 = np.sin(2 * np.pi * t / N * fc) * 0
    wave1 = np.sin(2 * np.pi * t / N * fc)
    for i in signal:
        if i == 0:
            ask.extend(wave0)
        else:
            ask.extend(wave1)
    return ask

def f_shift_key(fc):
    fsk = []
    wave0 = np.sin(2 * np.pi * t / N * (fc-2))
    wave1 = np.sin(2 * np.pi * t / N * fc)
    for i in signal:
        if i == 0:
            fsk.extend(wave0)
        else:
            fsk.extend(wave1)
    return fsk

def p_shift_key(fc):
    psk = []
    wave0 = np.sin(2 * np.pi * t / N * fc)
    wave1 = np.sin(np.pi + 2 * np.pi * t / N * fc)
    for i in signal:
        if i == 0:
            psk.extend(wave0)
        else:
            psk.extend(wave1)
    return psk

if __name__ == "__main__":
    main()
