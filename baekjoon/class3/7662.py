import heapq
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    heap_min = []
    heap_max = []
    k = int(input())
    for _ in range(k):
        operation, number = map(str, input().split())
        number = int(number)
        if operation == "I":
            heapq.heappush(heap_min, number)
            heapq.heappush(heap_max, (-number, number))
        elif operation == "D":
            if number == -1 and heap_min:
                n = heapq.heappop(heap_min)
                heap_max.remove((-n, n))
            elif number == 1 and heap_max:
                heap_min.remove(heapq.heappop(heap_max)[1])
    if heap_min:
        print(f"{heapq.heappop(heap_max)[1]} {heapq.heappop(heap_min)}")
    else:
        print("EMPTY")
