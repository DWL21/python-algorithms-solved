import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input())

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def make_routes(R, C, a, b, visited):
    result = []
    for i, j in directions:
        x = a + i
        y = b + j
        if 0 <= x and x < R and 0 <= y and y < C and not board[x][y] in visited:
            result.append((x, y))
    return result

queue = set([(0, 0, board[0][0])])
maximum = 0
while queue:
    x, y, visited = queue.pop()
    maximum = max(maximum, len(visited))
    for i, j in make_routes(R, C, x, y, visited):
        queue.add((i, j, visited + board[i][j]))
print(maximum)
    
