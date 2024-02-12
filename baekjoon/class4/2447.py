N = int(input())


def write_stars(n):
    if n == 3:
        board = [[1] * 3 for _ in range(3)]
        board[1][1] = 0
        return board
    k = n // 3
    board = [[0] * n for _ in range(n)]
    result = write_stars(k)
    for i in range(3):
        for j in range(3):
            ik = i*k
            jk = j*k
            if i == 1 and j == 1:
                continue
            for loop in range(k):
                board[ik + loop][jk:jk + k] = result[loop]
    return board


result = write_stars(N)


def star(x):
    if x:
        return '*'
    return ' '


for i in result:
    print(''.join(map(star, i)))
