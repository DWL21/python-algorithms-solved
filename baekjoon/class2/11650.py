import sys


input = sys.stdin.readline

N = int(input())
coordinates = list()
for _ in range(N):
    coordinates.append(tuple(map(int, input().split())))
coordinates.sort(key= lambda coordinate: (coordinate[0], coordinate[1]))
for x, y in coordinates:
    print(x, y)
