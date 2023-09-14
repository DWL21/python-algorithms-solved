import sys
import heapq

input = sys.stdin.readline

T = int(input())
heap = []
for _ in range(T):
    n = int(input())
    if n == 0:
        try:
            answer = heapq.heappop(heap)[1]
        except:
            answer = 0
        print(answer)
    if n != 0:
        heapq.heappush(heap, (abs(n), n))
