import sys


input = sys.stdin.readline

N = int(input())
boxes = [0] * 10001
for _ in range(N):
    boxes[int(input())] += 1
for i in range(10001):
    for _ in range(boxes[i]):
        print(i)
