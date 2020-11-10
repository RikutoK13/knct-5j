# 上三角行列になるまで行をたしあわせる。
# n*n行列とする(あとで改良する)

import numpy as np



ary = np.array([[2.0, 3.0, 4.0],
                   [3.0, 5.0, 2.0],
                   [4.0, 3.0, 30.0]])
ans = [6.0, 5.0, 32.0]  #

def main():
    del_times = 0
    in_times = 0
    row = len(ary)
    column = [len(n) for n in ary]
    vec = np.zeros(column[0])

    for n in range(column[0]):  # 上三角行列をつくる
        for m in range(row):
            if row-1-m != n:
                div = ary[row-1-m][n] / ary[n][n]
            else:
                div = 0
            # print(row-1-m)
            ans[row-1-m] -= div * ans[n]
            for k in range(column[n]):
                ary[row-1-m][k] -= div * ary[n][k]
                del_times += 1

    for a in range(row):  # 交代代入(n*mは未実装,3*3ならok)
        vec[row-1-a] = ans[row-1-a] / ary[row-1-a][row-1-a]
        in_times += 1

    print(ary)
    print("solution:", vec)
    print("num of calculation:", del_times + in_times)


if __name__ == "__main__":
    main()