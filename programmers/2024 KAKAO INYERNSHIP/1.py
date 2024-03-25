from collections import defaultdict
from itertools import combinations


GUEST = 'guest'

def is_winner(a, b, points, histories):
    ab = f'{a} {b}'
    ba = f'{b} {a}'
    if histories[ab] == histories[ba] and points[a] == points[b]:
        return GUEST
    if histories[ab] == histories[ba]:
        if points[a] > points[b]:
            return a
        return b
    if histories[ab] > histories[ba]:
        return a
    return b


def solution(friends, gifts):
    points = defaultdict(int)
    histories = defaultdict(int)
    for i in gifts:
        A, B = i.split()
        points[A] += 1
        points[B] -= 1
        histories[i] += 1
    result = defaultdict(int)
    for i, j in list(combinations(friends, 2)):
        result[is_winner(i, j, points, histories)] += 1
    result[GUEST] = 0
    return max(result.values())

