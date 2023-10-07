def solution(n):
    dictionary = dict()
    rank = 1
    for i in range(1, n + 1):
        while rank % 3 == 0 or '3' in str(rank):
            rank += 1
        dictionary[i] = rank
        rank += 1
    return dictionary[n]

print(solution(15))