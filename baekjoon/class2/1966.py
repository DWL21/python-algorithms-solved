import sys
import collections


input = sys.stdin.readline

cases_number = int(input())
for _ in range(cases_number):
    N, M = map(int, input().split())
    priorities = collections.deque(list(enumerate(map(int, input().split()))))
    count = 0
    while True:
        now = priorities.popleft()
        if len(priorities) != 0 and max(priorities, key=lambda x: x[1])[1] > now[1]:
            priorities.append(now)
        else:
            count += 1
            if now[0] == M:
                print(count)
                break
