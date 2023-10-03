def solution(num_list):
    odd = len(list(filter(lambda x: x % 2 , num_list)))
    return [len(num_list) - odd, odd]
