def solution(my_string):
    return sum(list(map(int, filter(lambda x: x.isdigit(), my_string))))
