from itertools import combinations
from collections import defaultdict
from itertools import product

def integrate(dices):
    total = defaultdict(int)
    for i in list(product(range(6), repeat=len(dices))):
        now = 0
        for j in range(len(dices)):
            now += dices[j][i[j]]
        total[now] += 1
    return total


def score(A, B):
    cases = []
    A_keys = sorted(list(A.keys()))
    B_keys = sorted(list(B.keys()))
    pointer = 0
    for i in A_keys:
        while pointer < len(B_keys) and i > B_keys[pointer]:
            pointer += 1
        if not pointer:
            continue
        cases.append((i, B_keys[pointer - 1]))
    B_total = defaultdict(int)
    B_total[B_keys[0]] = B[B_keys[0]]
    for i in range(1, len(B_keys)):
        B_total[B_keys[i]] = B_total[B_keys[i - 1]]
        B_total[B_keys[i]] += B[B_keys[i]]
    total = 0
    for i, j in cases:
        total += A[i] * B_total[j]
    return total


def solution(dice):
    n = len(dice)
    cases = list(combinations(dice, n // 2))
    dices = list(map(lambda x: integrate(x), cases))
    numbers = list(combinations(range(1, n + 1), n // 2))
    answer = []
    for i in range(len(cases)):
        A = dices[i]
        B = dices[-(i + 1)]
        answer.append(score(A, B))
    maximum_index = answer.index(max(answer))
    return list(numbers[maximum_index])
    

dices = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
print(solution(dices))
