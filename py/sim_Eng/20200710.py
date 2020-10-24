# 3*3の連立一次方程式を解く。パッケージ化してるけど汎用的でないので、暇なときにやる。
# 似てるプログラムあったら追記

import numpy as np



def main():
    matrix = np.array([[2, 3, 4], [3, 5, 2], [4, 3, 30]])
    x = [6, 5, 32]
    rmatrix = np.linalg.inv(matrix)

    solution = rmatrix @ x
    print(solution)

if __name__ == "__main__":
    main()