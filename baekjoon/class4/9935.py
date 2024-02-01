S = input()
bomb1 = list(input())

if len(bomb1) == 1:
    result = []
    for i in S:
        if i != bomb1[0]:
            result.append(i)
    print(''.join(map(str, result)))
    exit(0)

bomb2 = bomb1[:-1]
LENGTH = len(bomb1)

stack = []
for i in S:
    if i == bomb1[-1] and stack[-LENGTH + 1:] == bomb2:
        del stack[-LENGTH + 1:]
        while stack[-LENGTH:] == bomb1:
            del stack[-LENGTH:]
    else:
        stack.append(i)


if stack:
    print(''.join(map(str, stack)))
else:
    print("FRULA")
