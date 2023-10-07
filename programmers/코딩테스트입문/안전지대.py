directions = [
    (0, 0), (1, 1), (1, -1),
    (-1, -1), (-1, 1), (0, 1),
    (1, 0), (-1, 0), (0, -1)
    ]


def get_zones(size, i, j):
    zones = []
    for x, y in directions:
        a = i + x
        b = j + y
        if 0 <= a and a < size and 0 <= b and b < size:
            zones.append((a, b))
    return zones


def solution(board):
    dangerous_zones = [[0] * len(board) for _ in range(len(board))]
    for i, value in enumerate(board):
        for j, mine in enumerate(value):
            if mine:
                for x, y in get_zones(len(board), i, j):
                    dangerous_zones[x][y] = 1
    answer = 0
    for i in dangerous_zones:
        answer += sum(i)
    return len(board) ** 2 - answer
