plus = '+'
minus = '-'
def solution(my_string):
    answer = 0
    my_string = list(my_string.split())
    for i, value in enumerate(my_string):
        if value.isdigit() and (i == 0 or my_string[i - 1] is plus):
            answer += int(value)
        elif value.isdigit() and my_string[i - 1] is minus:
            answer -= int(value)
    return answer

print(solution("3 + 4"))