import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sites = dict()
for _ in range(N):
    name, value = map(str, input().rstrip().split())
    sites[name] = value
for _ in range(M):
    name = input().rstrip()
    print(sites[name])
