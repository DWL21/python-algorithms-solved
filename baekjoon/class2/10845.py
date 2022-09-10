import sys
import collections


input = sys.stdin.readline

queue = collections.deque()
N = int(input())
for _ in range(N):
    command = list(input().split())
    length = len(command)
    if length and command[0] == "pop":
        if len(queue) >= 1:
            print(queue.popleft())
        else:
            print(-1)
    elif length == 1 and command[0] == "size":
        print(len(queue))
    elif length == 1 and command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif length == 1 and command[0] == "front":
        if len(queue) >= 1:
            print(queue[0])
        else:
            print(-1)
    elif length == 1 and command[0] == "back":
        if len(queue) >= 1:
            print(queue[-1])
        else:
            print(-1)
    elif length == 2 and command[0] == "push":
        queue.append(int(command[1]))
