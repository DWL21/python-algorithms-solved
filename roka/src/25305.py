import sys

input = sys.stdin.readline

N, k = map(int, input().split())
records = list(map(int, input().split()))
records.sort(reverse=True)
print(records[k-1])
