N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
cheese = []
blanks = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j]:
            cheese.append((i, j))
        else:
            blanks.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def count_airs(board, visited):
    N = len(board)
    M = len(board[0])
    board_counting = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] or board[i][j]:
                continue
            for k in range(4):
                new_x = i + dx[k]
                new_y = j + dy[k]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                    continue
                board_counting[new_x][new_y] += 1
    return board_counting


def delete_cheese(board, board_counting):
    for i in range(N):
        for j in range(M):
            if board_counting[i][j] >= 2:
                board[i][j] = 0
    return board
                    
        
def bfs(board):
    N = len(board)
    M = len(board[0])
    visited = [[0] * M for _ in range(N)]
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        if visited[x][y] :
            continue
        visited[x][y] = 1
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M or board[new_x][new_y]:
                continue
            stack.append((new_x, new_y))
    return visited


def detect_cheese(board):
    N = len(board)
    M = len(board[0])
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                return True
    return False


times = 0
while detect_cheese(board):
    board_counting = count_airs(board, bfs(board))
    delete_cheese(board, board_counting)
    times += 1
print(times)

    



    
