# cording: utf-8
# 2020 6/12 simulation engineering
# はさみうち法により,√2の値を求めるプログラム
# Improvements about matplotlib below
# matplotlibを使ったことないので表示のやり方がわからないからここに書く
# 横軸が試行回数、縦軸が解析値
# 縦軸をもっと細かく表示したいけど、よくわからない(えぐい表示になる)

import numpy as np
import sys
import matplotlib.pyplot as plt

PRECISION = 20  # 計算回数
xnodes = list(range(PRECISION))  # プロット用計算回数
ynodes = []  # 解析値いれとくやつ

def main():
    minin = 0.0  # 初期値,minin~maxinの間にないと求められない
    maxin = 2.0

    if(0.0 < func_f(minin)):  # 初期値範囲エラー
        print("please set min value more lower")
        sys.exit()
    if(0.0 > func_f(maxin)):
        print("please set min value more lower")
        sys.exit()

    ans = func_split(minin, maxin)
    print('{} {}'.format(ans, ans - np.sqrt(ans)))  # 解析値とnumpyによる解析値の差(なんか変)

    plt.plot(xnodes, ynodes, marker='o')  # プロット,暇なときに関数化してみやすくする,暇な時間はない.
    plt.yticks(np.arange(1, 1.5, 0.05))  # 目盛設定,細かすぎると死ぬ,0.01でも重たい
    plt.show()

def func_f(x):  # 方程式(非線形に対応)
    return x**2.0 -2.0

def func_split(minin, maxin):  # 解析値もとめる関数,めんどいからコメントなし,多分あってる

    for times in range(PRECISION):
        node = (minin*func_f(maxin)-maxin*func_f(minin))/(func_f(maxin)-func_f(minin))
        print(node)
        if func_f(node) < 0:
            minin = node
        elif func_f(node) > 0:
            maxin = node
        else:
            times = PRECISION
        ynodes.append(node)
        print('node:{} max:{} min:{}'.format(node, maxin, minin))
    return node


main()

