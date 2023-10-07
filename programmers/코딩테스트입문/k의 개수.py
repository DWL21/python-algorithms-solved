def solution(i, j, k):
    k = str(k)
    times = 0
    for x in range(i, j + 1):
        times += str(x).count(k)
    return times
