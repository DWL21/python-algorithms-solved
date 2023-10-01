import sys

input = sys.stdin.readline


N, M = map(int, input().split())
numbers = [[0] * (N + 1)]
for _ in range(N):
    numbers.append([0] + list(map(int, input().split())))
cases = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    cases.append([(x1, y1), (x2, y2)])
for i in range(2, N + 1):
    numbers[i][1] += numbers[i - 1][1]
    numbers[1][i] += numbers[1][i - 1]
for i in range(2, N + 1):
    for j in range(2, N + 1):
        numbers[i][j] += (numbers[i - 1][j] + numbers[i][j - 1] - numbers[i - 1][j - 1])
for a, b in cases:
    answer = numbers[b[0]][b[1]] - numbers[a[0] - 1][b[1]] - numbers[b[0]][a[1] - 1] + numbers[a[0] - 1][a[1] - 1]
    print(answer)
