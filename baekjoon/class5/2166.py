import sys

input = sys.stdin.readline

N = int(input())
coordinates = []
for _ in range(N):
    coordinates.append(tuple(map(int, input().split())))
standard = coordinates[0]


def size(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)) / 2


def round_4(n):
    if n >= 0.5 + int(n):
        return int(n) + 1
    return int(n)

total = 0
for i in range(1, N - 1):
    total += size(standard, coordinates[i], coordinates[i + 1])

print(round_4(abs(total) * 10) / 10)
