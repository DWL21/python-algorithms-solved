import heapq
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    heap = []
    for _ in range(k):
        command, value = map(str, input().split())
        if command == "I":
            heapq.heappush(heap, int(value))
        elif value == "-1" and heap:
            heapq.heappop(heap)
        elif value == "1" and heap:
            heap = heapq.nlargest(len(heap), heap)[1:]
            heapq.heapify(heap)
    if heap:
        print(f"{heap[-1]} {heap[0]}")
    else:
        print("EMPTY")
