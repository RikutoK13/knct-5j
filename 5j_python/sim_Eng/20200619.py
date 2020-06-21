# 2020 6/19 simulation engineering
# ニュートン法により,√2の値を求めるプログラム\
# 横軸が試行回数、縦軸が解析値
# 縦軸をもっと細かく表示したいけど、よくわからない(えぐい表示になる)

import numpy as np
import sys
from sympy import *
import matplotlib.pyplot as plt

PRECISION = 20  # 計算回数
xnodes = list(range(PRECISION))  # プロット用計算回数
ynodes = []  # 解析値いれとくやつ

def main():

    val = 2.0
    ans = func_newton(val)
    #print('{} {}'.format(ans, ans - np.sqrt(ans)))  # 解析値とnumpyによる解析値の差(なんか変)

    print(ans)
    plt.plot(xnodes, ynodes, marker='o')  # プロット,暇なときに関数化してみやすくする,暇な時間はない.
    plt.yticks(np.arange(1, 1.5, 0.05))  # 目盛設定,細かすぎると死ぬ,0.01でも重たい
    plt.show()

def func_f(x, order):  # 方程式(非線形に対応)
    y, t = symbols('y, t')
    y = t**2.0 - 2.0
    for times in range(order):
        y = y.diff(t)

    yprime = y.subs(t, x)
    return yprime

def func_newton(vals):
    for times in range(PRECISION):
        nextval = vals - (func_f(vals, 0)/func_f(vals, 1))
        ynodes.append(vals)
        if nextval == vals:
            times = PRECISION
        else:
            vals = nextval
    return vals

main()

