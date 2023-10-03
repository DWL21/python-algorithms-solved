VOWELS = ['a', 'e', 'i', 'o', 'u']


def solution(my_string):
    return ''.join(filter(lambda x: x not in VOWELS, my_string))
    