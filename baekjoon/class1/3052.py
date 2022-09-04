import collections


numbers = list()
usage = collections.defaultdict(bool)
for _ in range(10):
    numbers.append(int(input()) % 42)
answer = 0
for i in numbers:
    if not usage[i]:
        usage[i] = True
        answer += 1
print(answer)
