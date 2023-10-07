def solution(emergency):
    answer = [0] * (len(emergency))
    result = list(enumerate(emergency))
    result.sort(key=lambda x: -x[1])
    result = list(enumerate(map(lambda x: x[0], result)))
    for i, value in result:
        answer[value] = i + 1
    return answer
