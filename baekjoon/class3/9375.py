from collections import defaultdict


n = int(input())
for _ in range(n):
    clothes = defaultdict(int)
    k = int(input())
    for _ in range(k):
        a, b = map(str, input().split())
        clothes[b] += 1
    answer = 1
    for i in clothes.values():
        answer *= (i + 1)
    answer -= 1
    print(answer)
