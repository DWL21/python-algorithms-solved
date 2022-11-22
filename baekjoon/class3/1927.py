import sys
import heapq

input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    number = int(input())
    if number:
        heapq.heappush(heap, number)
    elif heap:
        print(heapq.heappop(heap))
    else:
        print(0)
