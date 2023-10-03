to_alpha = dict()
alpha = 'abcdefghij'
for i in range(10):
    to_alpha[str(i)] = alpha[i]


def solution(age):
    return ''.join(map(lambda x: to_alpha[x], str(age)))
