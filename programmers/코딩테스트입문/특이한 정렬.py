def solution(numlist, n):
    numlist.sort(key=lambda x: (max(n - x, x - n), -x))
    return numlist