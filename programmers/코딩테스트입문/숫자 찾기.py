def solution(num, k):
    answer = str(num).find(str(k))
    if answer == -1:
        return -1
    return answer + 1
