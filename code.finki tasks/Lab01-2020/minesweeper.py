def right(matrix, i, j, n):
    if j + 1 == n:
        return 0
    else:
        if matrix[i][j + 1] == '#':
            return 1
        else:
            return 0


def top(matrix, i, j, n):
    if i == 0:
        return 0
    else:
        if matrix[i - 1][j] == '#':
            return 1
        else:
            return 0


def down(matrix, i, j, n):
    if i + 1 == n:
        return 0
    else:
        if matrix[i + 1][j] == '#':
            return 1
        else:
            return 0


def left(matrix, i, j, n):
    if j == 0:
        return 0
    else:
        if matrix[i][j - 1] == '#':
            return 1
        else:
            return 0


def diagonaltopright(matrix, i, j, n):
    if j + 1 == n or i == 0:
        return 0
    else:
        if matrix[i - 1][j + 1] == "#":
            return 1
        else:
            return 0


def diagonaltopleft(matrix, i, j, n):
    if j == 0 or i == 0:
        return 0
    else:
        if matrix[i - 1][j - 1] == '#':
            return 1
        else:
            return 0


def diagonalbottomleft(matrix, i, j, n):
    if i + 1 == n or j == 0:
        return 0
    else:
        if matrix[i + 1][j - 1] == '#':
            return 1
        else:
            return 0


def diagonalbottomright(matrix, i, j, n):
    if i + 1 == n or j + 1 == n:
        return 0
    else:
        if matrix[i + 1][j + 1] == '#':
            return 1
        else:
            return 0


if __name__ == '__main__':
    matrix = []
    g

    n = int(input())
    for i in range(0, n):
        s = input()
        li = s.split("   ")
        matrix.append(li)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                continue
            else:
                object = right(matrix, i, j, n) + top(matrix, i, j, n) + down(matrix, i, j, n) + left(matrix, i, j,
                                                                                                      n) + diagonaltopright(
                    matrix, i, j, n) + diagonaltopleft(matrix, i, j, n) + diagonalbottomleft(matrix, i, j,
                                                                                             n) + diagonalbottomright(
                    matrix, i, j, n)
                matrix[i][j] = str(object)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j + 1 == len(matrix[i]):
                print(matrix[i][j])
            else:
                print(matrix[i][j] + "   ", end='')
