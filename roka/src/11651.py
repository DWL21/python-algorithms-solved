import sys

input = sys.stdin.readline

coordinates = []
N = int(input())
for _ in range(N):
    coordinates.append(tuple(map(int, input().split())))
coordinates.sort(key= lambda x: (x[1], x[0]))
for x, y in coordinates:
    print(f"{x} {y}")
