import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    heap_left = []
    heap_right = []
    histories = defaultdict(int)
    k = int(input())
    for _ in range(k):
        operation, number = map(str, input().split())
        number = int(number)
        if operation == "I":
            heapq.heappush(heap_left, number)
            heapq.heappush(heap_right, -number)
            histories[number] += 1
        elif operation == "D" and number == -1 and heap_left:
            histories[heapq.heappop(heap_left)] -= 1
        elif number == 1 and heap_right:
            histories[-heapq.heappop(heap_right)] -= 1
    flag = False
    while heap_left:
        minimum = heapq.heappop(heap_left)
        flag = True
        if histories[minimum] >= 1:
            flag = False
            break
    if flag:
        print("EMPTY")
        continue
    while heap_right:
        maximum = heapq.heappop(heap_right)
        flag = True
        if histories[maximum] >= 1:
            flag = False
            break
    if flag:
        print("EMPTY")
        continue
    print(f"{maximum} {minimum}")
