n = int(input())
stack = []
now = 1
answer = []
success = True
for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        answer.append("+")
        now += 1
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        success = False
        break
if success:
    for i in answer:
        print(i)
else:
    print("NO")
