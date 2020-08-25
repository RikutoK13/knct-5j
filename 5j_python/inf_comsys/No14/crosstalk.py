import math
import numpy as np
import matplotlib.pyplot as plt



M = 1000000

def main():
    frequency = np.zeros(200)
    cross_talk = np.zeros(200)
    ne_cross_talk = np.zeros(200)
    fe_cross_talk = np.zeros(200)

    for times in range(200):
        frequency[times] = (times * 0.5 + 1)
        cross_talk[times] = 1.967 * math.sqrt(frequency[times]) + 0.023 * frequency[times] + 0.050 / math.sqrt((frequency[times]))
        ne_cross_talk[times] = 35.3 - 15 * math.log10(frequency[times] / 100)
        fe_cross_talk[times] = 23.8 - 20 * math.log10(frequency[times] / 100)


    print(cross_talk[0])
    print(cross_talk[3])
    print(cross_talk[18])
    print(cross_talk[38])
    print(cross_talk[48])
    print(cross_talk[60])
    print(cross_talk[123])
    print(cross_talk[198])
    plt.subplot(3, 1, 1)
    plt.plot(frequency, cross_talk)
    plt.subplot(3, 1, 2)
    plt.plot(frequency, ne_cross_talk)
    plt.subplot(3, 1, 3)
    plt.plot(frequency, fe_cross_talk)
    plt.show()



if __name__ == "__main__":
    main()


