from collections import defaultdict
from itertools import permutations


def distance(x, y):
    if x != y:
        return 1
    return 0


def minimum_distance(case):
    x, y, z = case
    total = 0
    for i in range(4):
        total += (distance(x[i], y[i]) + distance(y[i], z[i]) + distance(x[i], z[i]))
    return total
        

def answer(people, categories):
    if max(categories.values()) >= 3:
        return 0
    minimum = 16
    cases = permutations(people, 3)
    for i in cases:
        minimum = min(minimum, minimum_distance(i))
        if minimum == 2:
            return minimum
    return minimum


T = int(input())
for _ in range(T):
    n = int(input())
    people = list(input().split())
    categories = defaultdict(int)
    for i in people:
        categories[i] += 1
    print(answer(people, categories))

