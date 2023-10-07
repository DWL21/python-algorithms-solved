from collections import defaultdict


def solution(s):
    dictionary = defaultdict(int)
    for i in s:
        dictionary[i] += 1
    return ''.join(sorted(list(map(lambda x: x[0], filter(lambda x: x[1] == 1, dictionary.items())))))
