def solution(my_string):
    return list(sorted(list(map(int, filter(lambda x: x.isdigit(), my_string)))))
