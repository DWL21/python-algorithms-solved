def solution(my_str, n):
    answer = []
    for i in range(0, (len(my_str) - 1) // n + 1):
        answer.append(my_str[i * n: (i + 1) * n])
    return answer
