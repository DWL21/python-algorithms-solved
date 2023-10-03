ROCK = '0'
PAPER = '5'
SCISSORS = '2'


def win(case):
    if case == ROCK:
        return PAPER
    if case == SCISSORS:
        return ROCK
    return SCISSORS


def solution(rsp):
    return ''.join(map(win, rsp))
