def solution(my_string):
    answer = []
    for i in my_string:
        if i.isupper():
            answer.append(i.lower())
            continue
        answer.append(i.upper())
    return ''.join(answer)
