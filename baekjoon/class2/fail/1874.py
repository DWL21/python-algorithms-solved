import sys

input = sys.stdin.readline

N = int(input())
numbers = list()
for _ in range(N):
    numbers.append(int(input()))
left = 0
stack = list()
histories = list()

n = 1
able = True

for i in range(1, N + 1):
    if stack:
        if numbers[left] == stack[-1]:
            while stack and numbers[left] == stack[-1]:
                stack.pop()
                histories.append("-")
                left += 1
            stack.append(i)
            histories.append("+")
        elif numbers[left] > stack[-1]:
            stack.append(i)
            histories.append("+")
        else:
            able = False
            break
    else:
        stack.append(i)
        histories.append("+")

if able:
    for i in range(left, N):
        histories.append('-')
    for i in histories:
        print(i)
else:
    print("NO")
