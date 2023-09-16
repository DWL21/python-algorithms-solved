from collections import deque

RED = 'R'
GREEN = 'G'
BLUE = 'B'

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
N = int(input())
drawings = []
for _ in range(N):
    drawings.append([i for i in input()])

def road(i, j, drawings):
    roads = []
    for x, y in direction:
        if i+x >= 0 and i+x < N and j+y >= 0 and j+y < N and drawings[i][j] == drawings[i+x][j+y]:
            roads.append((i+x, j+y))
    return roads

def solution(drawings, N):
    times = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            queue = deque([(i, j)])
            if not visited[i][j]:
                times += 1
                while queue:
                    x, y = queue.popleft()
                    if not visited[x][y]:
                        visited[x][y] = True
                        queue.extend(road(x, y, drawings))
    return times

a = str(solution(drawings, N))
for i in range(N):
    for j in range(N):
        if drawings[i][j] is RED:
            drawings[i][j] = GREEN
b = str(solution(drawings, N))

print(a + " " + b)
