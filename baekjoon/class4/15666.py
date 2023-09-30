from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
sequences = sorted(list(set(combinations_with_replacement(numbers, M))))

for sequence in sequences:
    print(' '.join(map(str, sequence)))
        
