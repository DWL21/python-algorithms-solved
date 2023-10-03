def solution(n):
    answer = 0
    while True:
        answer += 1
        if not (6 * answer) % n:
            return answer
