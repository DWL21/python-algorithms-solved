PLUS = '+'
MINUS = '-'
CORRECT = 'O'
FAILED = 'X'


def solution(quiz):
    result = []
    for i in quiz:
        X, operater, Y, _, Z = i.split()
        if operater is PLUS:
            if int(X) + int(Y) == int(Z):
                result.append(CORRECT)
                continue
        if operater is MINUS:
            if int(X) - int(Y) == int(Z):
                result.append(CORRECT)
                continue
        result.append(FAILED)
    return result
