LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

def solution(keyinput, board):
    n, m = board
    n //= 2
    m //= 2
    x = 0
    y = 0
    for i in keyinput:
        if i == UP and y < m:
            y += 1
        elif i == DOWN and y > -m:
            y -= 1
        elif i == LEFT and x > -n:
            x -= 1
        elif i == RIGHT and x < n:
            x += 1
    return [x, y]
