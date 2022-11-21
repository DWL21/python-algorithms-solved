import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    points = []
    sections = []
    for _ in range(K):
        points.append(list(map(int, input().split())))
