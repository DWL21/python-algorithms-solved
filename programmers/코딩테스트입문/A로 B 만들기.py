from collections import defaultdict


def solution(before, after):
    dictionary = defaultdict(int)
    for i in before:
        dictionary[i] += 1
    for i in after:
        if dictionary[i] <= 0:
            return 0
        dictionary[i] -= 1
    return 1

        