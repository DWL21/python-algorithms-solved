def solution(order):
    return len(list(filter(lambda x: x in ['3', '6', '9'], str(order))))
