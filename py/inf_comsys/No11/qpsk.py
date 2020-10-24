import numpy as np
import matplotlib.pyplot as plt


N = 128
t = np.arange(0, N, 1)
fc = 2
# 下記の信号はデジタル信号 [1,0,0,0,1,1,1,0]
# signal = [1, -1, -1, -1, 1, 1, 1, -1]
signal = [[0, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0]]
# print("*** only space separated***")
# signal = input().split()
# print(signal)
# for times in range(len(signal)):
    # signal[times] = int(signal[times])
psk = []
wave0 = np.cos(2 * np.pi * t / N * fc)
wave1 = np.cos((2 * np.pi * t / N * fc) + np.pi)
for i in signal:
    if i == 1:
        psk.extend(wave0)
    else:
        psk.extend(wave1)
# 復調用の波形
hukutyou = []
for i in range(len(signal)):
    # hukutyou.extend(np.cos(2*np.pi*t/N*fc))
    if signal[0][1] == 0:
        hukutyou.extend((-1)**i * np.cos(2 * np.pi * t / N * fc))
    if signal[i][1] == 1:
        hukutyou.extend((-1)**i * np.sin(2 * np.pi * t / N * fc))

psk = np.array(psk)
hukutyo = np.array(hukutyou)
psk *= hukutyou
psk = np.fft.fftshift(psk)
psk = np.fft.fft(psk)
psk = np.fft.fftshift(psk)
psk[:512 - 16] = 0
psk[512 + 16:] = 0
psk = np.fft.fftshift(psk)
psk = np.fft.ifft(psk)
psk = np.fft.fftshift(psk)
plt.plot(range(len(psk)), psk)
plt.show()
