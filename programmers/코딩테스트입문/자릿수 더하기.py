def solution(my_string, letter):
    return ''.join(filter(lambda x: x is not letter, my_string))
