def solution(common):
    if common[2] - common[1] == common[1] - common[0]:
        return 2 * common[-1] - common[-2]
    return common[-1] ** 2 // common[-2]
