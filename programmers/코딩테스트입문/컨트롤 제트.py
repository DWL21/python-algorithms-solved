undo_letter = "Z"


def solution(s):
    answer = 0
    record = 0
    for i in s.split():
        if i == undo_letter:
            answer -= record
            continue
        answer += int(i)
        record = int(i)
    return answer
