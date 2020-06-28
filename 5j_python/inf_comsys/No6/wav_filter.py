# 演習課題では,-1000~1000Hzの周波数をカットした
# サンプル数882000,間隔は1/44.1kHzなので、0.05ぐらい
# 0.05*20000点で1000Hz,それを+-0対象にすると-1000~1000Hzぐらい

import wave
import array
import numpy as np
from matplotlib import pylab as plt

##################
# load wav file
##################
wr = wave.open("holst_mono_clip.wav", "rb")
print("Channel num : ", wr.getnchannels())
print("Sample size : ", wr.getsampwidth())
print("Sampling rate : ", wr.getframerate())
print("Frame num : ", wr.getnframes())
print("Sec : ", float(wr.getnframes()) / wr.getframerate())
n_sample = wr.getnframes()
f = wr.readframes(n_sample)
f = np.frombuffer(f, dtype="int16")
start_wav = int(0 * wr.getframerate())
end_wav = int(20.0 * wr.getframerate())
N = end_wav - start_wav
N_2 = int(N / 2)
f = f[start_wav:end_wav]

##################
# filter in frequency domain
##################
F = np.fft.fft(f)
F = np.fft.fftshift(F)
# original spectrum
plt.plot(range(len(F)), np.abs(F))
plt.show()
## low pass filter
F[0:N_2 - 15000] = 0
F[N_2 + 15000:-1] = 0
## filtered spectrum
plt.plot(range(len(F)), np.abs(F))
plt.show()

# high pass filter
F = np.fft.fft(f)
F = np.fft.fftshift(F)
# F[0:N_2 - 15000] = 0
# F[N_2 + 15000:-1] = 0
F[N_2-15000:N_2+15000] = 0
# filtered spectrum
plt.plot(range(len(F)), np.abs(F))
plt.show()

# any pass filter (cut loud sound)
F = np.fft.fft(f)
F = np.fft.fftshift(F)
F = np.abs(F)
F[N_2-20000:N_2+20000] = 0
# filtered spectrum
plt.plot(range(len(F)), np.abs(F))
plt.show()

# any pass filter (cut loud sound)
F = np.fft.fft(f)
F = np.fft.fftshift(F)
F = np.abs(F)
# F[N_2-15000:N_2+15000] = 0
wavmax = max(F)
for times in range((int(end_wav))):
    if F[times] > wavmax/2:
        F[times] = 0
# filtered spectrum
plt.plot(range(len(F)), np.abs(F))
plt.show()

# convert to time domain (?what?)
F = np.fft.fftshift(F)
f2 = np.fft.ifft(F)

##################
# save wav file
##################
w = wave.Wave_write("holst_mono_filtered.wav")
w.setparams((
    1,  # channel
    2,  # byte width
    wr.getframerate(),  # sampling rate
    wr.getnframes(),  # number of frames
    "NONE", "not compressed"  # no compression
))
w.writeframes(array.array('h', f2).tostring())
w.close()
