from itertools import combinations

A = 'bcdfghjklmnpqrstvwxyz'
B = 'aeiou'

indexing = dict()

for i, value in enumerate('abcdefghijklmnopqrstuvwxyz'):
    indexing[value] = i

L, C = map(int, input().split())
letters = list(input().split())


As = []
Bs = []

for i in letters:
    if i in B:
        Bs.append(i)
    else:
        As.append(i)

As.sort()
Bs.sort()

answer = []
for i in range(2, L):
    A_cases = list(combinations(As, i))
    B_cases = list(combinations(Bs, L - i))
    for j in A_cases:
        for k in B_cases:
            now = j + k
            answer.append(''.join(sorted(list(now), key=lambda x: indexing[x])))

answer.sort()
for i in answer:
    print(i)
