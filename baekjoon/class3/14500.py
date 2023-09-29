UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

blocks = [
    (RIGHT, RIGHT, RIGHT),
    (DOWN, DOWN, DOWN),
    (RIGHT, DOWN, LEFT),
    (DOWN, DOWN, RIGHT),
    (UP, RIGHT, RIGHT),
    (RIGHT, DOWN, DOWN),
    (DOWN, LEFT, LEFT),
    (DOWN, RIGHT, DOWN),
    (LEFT, DOWN, LEFT),
    (RIGHT, UP, UP),
    (DOWN, RIGHT, RIGHT),
    (UP, UP, RIGHT),
    (UP, LEFT, LEFT),
    (UP, RIGHT, UP),
    (LEFT, UP, LEFT)
    ]
directions = [UP, DOWN, LEFT, RIGHT]


def get_coordinate(x, y, direction):
    return (x + direction[0], y + direction[1])


def is_in_line(x, y, N, M):
    if 0 <= x and x < N and 0 <= y and y < M:
        return True
    return False


def calculate_point(x, y, block, board):
    point = board[x][y]
    for direction in block:
        x, y = get_coordinate(x, y, direction)
        if not is_in_line(x, y, N, M):
            return 0
        point += board[x][y]
    return point


def special_block(x, y, board):
    point = board[x][y]
    table = []
    for direction in directions:
        i, j = get_coordinate(x, y, direction)
        if not is_in_line(i, j, N, M):
            continue
        table.append(board[i][j])
    if len(table) <= 2:
        return 0
    return point + sum(sorted(table, reverse=True)[:3])


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

points = []
for i in range(N):
    for j in range(M):
        for block in blocks:
            points.append(calculate_point(i, j, block, board))
        points.append(special_block(i, j, board))
print(max(points))
