import sys

input = sys.stdin.readline

S = []
M = int(input())
for _ in range(M):
    command = list(map(str, input().rstrip().split()))
    if len(command) == 1:
        command_method = command[0]
        if command_method == "all":
            S = [i + 1 for i in range(20)]
        elif command_method == "empty":
            S = []
    elif len(command) == 2:
        command_method, x = command[0], int(command[1])
        if command_method == "add" and x not in S:
            S.append(x)
        elif command_method == "remove" and x in S:
            S.remove(x)
        elif command_method == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif command_method == "toggle":
            if x in S:
                S.remove(x)
            else:
                S.append(x)
