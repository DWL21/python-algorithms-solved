from collections import defaultdict


k = int(input())
computers = defaultdict(list)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

stack = [1]
index = 0
while index < len(stack):
    temp = computers[stack[index]]
    stack.extend(temp)
    temp.clear()
    index += 1
print(len(set(stack)) - 1)
