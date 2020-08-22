import numpy as np



ary = np.array([[2.0, 4.0, 6.0],
                   [1.0, 5.0, 15.0],
                   [4.0, 10.0, 21.0]])

ary_l = np.zeros((3, 3))
ary_u = np.zeros((3, 3))
vec = [20.0, 28.0, 53.0]

def main():
    times = 0  # 計算回数を記録
    times = lu_breakup(times)
    print(ary_l)
    print(ary_u)

    ans = proc_l()
    print('solution:', ans)
    print("num of calculation:", times + 6)  # どうせ代入で6回計算するので

def proc_l():  # ｌ行列を処理
    b_vec = np.zeros(3)
    b_vec[0] = vec[0]
    b_vec[1] = vec[1] - ary_l[1][0]*b_vec[0]
    b_vec[2] = vec[2] - ary_l[2][0]*b_vec[0] - ary_l[2][1]*b_vec[1]

    ans_vec = proc_u(b_vec)
    return ans_vec

def proc_u(b_vec):  # u行列を処理して,解を求める.
    ans_vec = np.zeros(3)

    ans_vec[2] = b_vec[2] / ary_u[2][2]
    ans_vec[1] = (b_vec[1] - ary_u[1][2]*ans_vec[2]) / ary_u[1][1]
    ans_vec[0] = (b_vec[0] - ary_u[0][1]*ans_vec[1] - ary_u[0][2]*ans_vec[2]) / ary_u[0][0]

    return ans_vec


def lu_breakup(times):  # LU分解(簡単のため,3*3に限定する)
    for row in range(3):  # rowとcolumnは+1で考える
        for column in range(3):
            if row == 0:  # 1行目
                ary_l[row][column] = 0
                ary_l[row][row] = 1
                ary_u[row][column] = ary[row][column]

            if row == 1:  # 2行目
                ary_l[row][column] = 0
                ary_l[row][row] = 1
                ary_l[row][0] = ary[row][0] / ary_u[0][0]
                if column >= row:
                    ary_u[row][column] = ary[row][column] - ary_u[row-1][column]*ary_l[row][row-1]
                if row < column:
                    ary_l[row][column] = 0

            if row == 2:  # 3行目
                ary_l[row][row] = 1
                ary_l[row][0] = ary[row][0] / ary_u[0][0]
                if column < row:
                    ary_l[row][column] = (ary[row][column] - ary_l[row][row-2]*ary_u[row-2][row-1]) / ary_u[row-1][row-1]
                if column >= row:
                    ary_u[row][column] = ary[row][column] - ary_u[row-2][row]*ary_l[row][row-2] - ary_u[row-1][row]*ary_l[row][row-1]
                if row < column:
                    ary_l[row][column] = 0
            times += 1
    return times


if __name__ == "__main__":
    main()