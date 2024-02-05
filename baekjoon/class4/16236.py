from collections import deque

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def find_shark(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                return (i, j, 0)
            

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

size = 2
counting = 0
time = 0

def bfs(N):
    visited = [[False] * N for _ in range(N)]
    a, b, c = find_shark(N)
    queue = deque([(a, b, c)])
    shortest_distance = int(1e5)
    fishes = []
    while queue:
        x, y, distance = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or board[new_x][new_y] == 9:
                continue
            new = board[new_x][new_y]
            if not new or new == size:
                queue.append((new_x, new_y, distance + 1))
            elif new < size and distance + 1 < shortest_distance:
                fishes = [(new_x, new_y)]
                shortest_distance = distance + 1
                queue.append((new_x, new_y, distance + 1))
            elif new < size and distance + 1 == shortest_distance:
                fishes.append((new_x, new_y))
                queue.append((new_x, new_y, distance + 1))
    return sorted(list(set(fishes))), shortest_distance


fishes, distance = bfs(N)
x, y, _ = find_shark(N)
board[x][y] = 0
while fishes:
    x, y = fishes[0]
    counting += 1
    time += distance
    if counting >= size:
        size += 1
        counting = 0
    board[x][y] = 9
    fishes, distance = bfs(N)
    board[x][y] = 0
else:
    print(time)
    
