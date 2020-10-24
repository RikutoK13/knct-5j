# 3*3のみ対応

from matplotlib import pyplot as plt


def test_jacobi():

    in_x = 0
    in_y = 0
    in_z = 0

    accuracy = 10

    a = [[7, 1, 2],
         [1, 8, 3],
         [2, 3, 9]]

    vec = [10, 8, 6]

    x, y, z = jacobi(a, vec, accuracy, in_x=in_x, in_y=in_y, in_z=in_z)
    a, b, c = gauss_seidel(a, vec, accuracy, in_x=in_x, in_y=in_y, in_z=in_z)

    print('Jacobi:')
    print(x)
    print(y)
    print(z)

    print('initial value:')
    print('x:{} y:{} z:{}'.format(in_x, in_y, in_z))

    print('ans:')
    n = len(x) - 1
    print(x[n], y[n], z[n])

    print('Gauss=Seidel:')
    print(a)
    print(b)
    print(c)

    print('initial value:')
    print('x:{} y:{} z:{}'.format(in_x, in_y, in_z))

    print('ans:')
    n = len(a) - 1
    print(a[n], b[n], c[n])

    row = list(range(n+1))
    plt.plot(row, x, label='Jacobi method')
    plt.plot(row, a, label='Gauss=Seidel method')
    plt.text(6.5, 0.2, 'initial value[x:{} y:{} z:{}]'.format(in_x, in_y, in_z))
    plt.xlabel('num of calc')
    plt.ylabel('value of x')
    # plt.plot(n, y)
    # plt.plot(n, z)
    plt.legend()
    plt.show()


def jacobi(matrix, vector, accuracy, in_x=0, in_y=0, in_z=0):
    """Jacobi methods for solving Ax = b"""

    x = [in_x]
    y = [in_y]
    z = [in_z]

    for n in range(accuracy):
        x.append((vector[0] - matrix[0][1] * y[n] - matrix[0][2] * z[n]) / matrix[0][0])
        y.append((vector[1] - matrix[1][0] * x[n] - matrix[1][2] * z[n]) / matrix[1][1])
        z.append((vector[2] - matrix[2][0] * x[n] - matrix[2][1] * y[n]) / matrix[2][2])

    return x, y, z


def gauss_seidel(matrix, vector, accuracy, in_x=0, in_y=0, in_z=0):
    """Gauss=Seidel methods for solving Ax = b"""

    x = [in_x]
    y = [in_y]
    z = [in_z]

    for n in range(accuracy):
        x.append((vector[0] - matrix[0][1] * y[n] - matrix[0][2] * z[n]) / matrix[0][0])
        y.append((vector[1] - matrix[1][0] * x[n+1] - matrix[1][2] * z[n]) / matrix[1][1])
        z.append((vector[2] - matrix[2][0] * x[n+1] - matrix[2][1] * y[n+1]) / matrix[2][2])

    return x, y, z


if __name__ == "__main__":
    test_jacobi()