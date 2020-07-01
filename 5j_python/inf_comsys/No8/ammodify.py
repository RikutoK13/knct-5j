# AM変調 A(a*s(t)+1)cos2pi(fct)
# 時間波形とスペクトルを観察
# !:Be careful of the path when importing

# --- 演習 ---
# キャリア周波数:一番振幅の大きいもの
# 上側波帯:キャリアの右側
# 下側波帯:キャリアの左側
# スペクトル減衰の理由:A(as(t)+1)にcosをかけることにより,0~1の範囲で減衰されるから.

import numpy as np
import matplotlib.pyplot as plt

SAMPLING_PERIOD = 128
PF = PRE_FREQUENCY = 4  # Hz
CF = CARRIER_FREQUENCY = 32  # Hz
A = 1  # amplitude
a = 1


def main():
    f = np.zeros((5, SAMPLING_PERIOD))
    t = np.arange(SAMPLING_PERIOD)
    for hz in range(5):
        for times in range(SAMPLING_PERIOD):
            f[hz][times] = A * (a * np.cos(2 * np.pi / (PF + hz) * times) + 1) * np.cos(2 * np.pi / CF * times)
        plt.subplot(2, 1, 1)
        plt.title(r"$\ AM $")
        plt.plot(t, f[hz])
        plt.subplot(2, 1, 2)
        plt.title(r"$\ Spectrum $")
        plt.plot(t, np.abs(f[hz]) ** 2)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
