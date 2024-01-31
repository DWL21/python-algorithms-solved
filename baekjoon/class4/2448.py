N = 3*2**int(input())

CENTER = (N*2 - 1) // 2
board = [[' ']*(N*2 - 1) for _ in range(N)]


def write_default_triangle(board, x, y):
    board[y][x] = '*'
    board[y + 1][x - 1] = '*'
    board[y + 1][x + 1] = '*'
    board[y + 2][x - 2] = '*'
    board[y + 2][x - 1] = '*'
    board[y + 2][x] = '*'
    board[y + 2][x + 1] = '*'
    board[y + 2][x + 2] = '*'


def write_star(board, depth, x, y):
    n = 3*2**depth
    if depth == 0:
        write_default_triangle(board, x, y)
    if depth > 0:
        write_star(board, depth - 1, x, y)
        write_star(board, depth - 1, x - (n - 1) // 2 - 1, y + n // 2)
        write_star(board, depth - 1, x + (n - 1) // 2 + 1, y + n // 2)


def cal_depth(N):
    for i in range(11):
        if 2 ** i == N // 3:
            return i


write_star(board, cal_depth(N), CENTER, 0)
for i in range(N):
    print(''.join(map(str, board[i])))
