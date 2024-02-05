import copy

R, C, T = map(int, input().split())
board = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(R):
    board.append(list(map(int, input().split())))

for i in range(R):
    if board[i][0] == -1:
        air = [i, i + 1]
        break

for _ in range(T):
    new_board = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] == 0:
                continue
            if board[x][y] == -1:
                new_board[x][y] = -1
                continue
            distributions = board[x][y] // 5
            new_board[x][y] += board[x][y]
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x < 0 or new_x >= R or new_y < 0 or new_y >= C or board[new_x][new_y] == -1:
                    continue
                new_board[new_x][new_y] += distributions
                new_board[x][y] -= distributions
            
    for i in range(air[0] - 1, 0, -1):
        new_board[i][0] = new_board[i - 1][0]
    new_board[0] = new_board[0][1:] + [0]
    for i in range(0, air[0]):
        new_board[i][C - 1] = new_board[i + 1][C - 1]
    new_board[air[0]] = [-1, 0] + new_board[air[0]][1:-1]

    for i in range(air[1] + 1, R - 1):
        new_board[i][0] = new_board[i + 1][0]
    new_board[R - 1] = new_board[R - 1][1:] + [0]
    for i in range(R - 1, air[1], -1):
        new_board[i][C - 1] = new_board[i - 1][C - 1]
    new_board[air[1]] = [-1, 0] + new_board[air[1]][1: -1]
    
    for i in new_board:
        print(' '.join(map(str, i)))

    board = copy.deepcopy(new_board)


result = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            result += board[i][j]
print(result)
