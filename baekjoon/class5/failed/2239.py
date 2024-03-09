
board = []
for _ in range(9):
    board.append(list(map(int, input())))

row = [[False] * 10 for _ in range(9)]
column = [[False] * 10 for _ in range(9)]
region = [[False] * 10 for _ in range(9)]


def get_region(i, j):
    return (i // 3)*3 + j // 3


def make_board_positions():
    result = []
    for i in range(9):
        for j in range(9):
            result.append((i, j))
    return result

positions = make_board_positions()

for i, j in positions:
    if not now:
        continue
    row[i][now] = True
    column[j][now] = True
    region[get_region(i, j)][now] = True


def exists_number(i, j):
    result = []
    for k in range(1, 10):
        if not row[i][k] and not column[j][k] and not region[get_region(i, j)][k]:
            result.append(k)
    return result

counting = 0
for i, j in positions:
    if now:
        continue
    numbers = exists_number(i, j)
    if numbers == 1:
        now = numbers[0]
        row[i][now] = True
        column[j][now] = True
        region[get_region(i, j)][now] = True
        counting += 1
    
