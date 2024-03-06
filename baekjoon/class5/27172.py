from collections import defaultdict

N = int(input())
cards = list(map(int, input().split()))
exists = defaultdict(bool)
for i in cards:
    exists[i] = True
points = defaultdict(bool)
for i in range(N):
    now = cards[i]
    for j in range(now, 10**6 + 1, now):
        if exists[j]:
            points[now] += 1
            points[j] -= 1
result = list(map(lambda x: points[x], cards))
print(' '.join(map(str, result)))
