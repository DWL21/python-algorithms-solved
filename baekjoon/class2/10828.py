import sys


input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    command = list(input().split())
    length = len(command)
    if length and command[0] == "pop":
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    elif length == 1 and command[0] == "size":
        print(len(stack))
    elif length == 1 and command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif length == 1 and command[0] == "top":
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)
    elif length == 2 and command[0] == "push":
        stack.append(command[1])
