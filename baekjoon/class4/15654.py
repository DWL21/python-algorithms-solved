from itertools import permutations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
cases = permutations(numbers, M)
for case in cases:
    print(" ".join(map(str, case)))
