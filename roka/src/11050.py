from itertools import combinations

N, K = map(int, input().split())
print(len(list(combinations(list(range(N)), K))))

