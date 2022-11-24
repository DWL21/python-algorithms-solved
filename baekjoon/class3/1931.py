import sys

input = sys.stdin.readline

N = int(input())

meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda value: (value[1], value[0]))
counting = 0
last = 0
for x, y in meetings:
    if last <= x:
        counting += 1
        last = y
print(counting)
