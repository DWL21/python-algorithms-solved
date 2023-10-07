from itertools import permutations


def solution(babbling):
    cases = []
    result = 0
    for i in range(1, 5):
        cases += list(permutations(["aya", "ye", "woo", "ma"], i))
    cases = list(map(lambda x: ''.join(x), cases))
    for i in babbling:
        if i in cases:
            result += 1
    return result

babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))