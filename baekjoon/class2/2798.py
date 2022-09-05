N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            result = cards[i] + cards[j] + cards[k]
            if not (i == j or j == k or k == i or result > M):
                answer = max(answer, result)
print(answer)
