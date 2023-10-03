RIGHT = 'right'
LEFT = 'left'

def solution(numbers, direction):
    if direction == RIGHT:
        return [numbers.pop()] + numbers
    return numbers + [numbers.pop(0)]
