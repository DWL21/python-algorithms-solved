def solution(my_string):
    letters = []
    answer = []
    for i in my_string:
        if not i in letters:
            answer.append(i)
            letters.append(i)
    return ''.join(answer)

