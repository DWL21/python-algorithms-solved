from itertools import permutations

N, M = map(int, input().split())
sequence = sorted(list(map(int, input().split())))
answer = sorted(list(set(permutations(sequence, M))))
for i in answer:
    print(' '.join(map(str, i)))


