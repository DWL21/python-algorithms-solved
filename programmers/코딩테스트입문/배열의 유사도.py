def solution(s1, s2):
    return len(list(filter(lambda x: x in s2, s1)))
