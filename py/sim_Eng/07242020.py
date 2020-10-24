# 上三角行列になるまで行をたしあわせる。

import numpy as np



ary = np.array([[2.0, 3.0, 4.0],
                   [3.0, 5.0, 2.0],
                   [4.0, 3.0, 30.0]])
vec = [6.0, 5.0, 32.0]

def main():
    times = 0
    row = len(ary)
    column = [len(n) for n in ary]
    subrow = row + 1

    for n in range(column[0]):  # 列数
        subrow -= 1
        for m in range(row-1):  # 列の
            if subrow-m-1 != n:
                div = ary[n][subrow-m-1] / ary[n][n]  # m行目-div*0行目をする
            else:
                div = 0
            print(div)
            for k in range(column[n]):
                if subrow-m-1 != n:
                    ary[subrow-m-1][k] -= div * ary[n][k]
                    times += 1
    print(ary)
    print(times)






if __name__ == "__main__":
    main()