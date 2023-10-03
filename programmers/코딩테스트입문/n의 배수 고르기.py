def solution(n, numlist):
    return list(filter(lambda x: not x % n, numlist))
