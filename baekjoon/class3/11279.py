import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    number = int(input())
    if number:
        heapq.heappush(heap, (-number, number))
    elif heap:
        print(heapq.heappop(heap)[1])
    else:
        print(0)
