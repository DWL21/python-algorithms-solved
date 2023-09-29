from itertools import product


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))


def is_valid(sequence):
    now = 0
    for i in sequence:
        if now > i:
            return False
        now = i
    return True

sequences = product(numbers, repeat=M)
for sequence in sequences:
    now = 0
    if is_valid(sequence):
        print(' '.join(map(str, sequence)))

