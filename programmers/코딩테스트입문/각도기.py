STANDARD = 90

def solution(angle):
    if angle < STANDARD:
        return 1
    if angle == STANDARD:
        return 2
    if angle < STANDARD * 2:
        return 3
    return 4
