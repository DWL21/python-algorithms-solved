from collections import deque


command_pop = 'D'
command_reverse = 'R'


def run(numbers, n):
    direction = 1
    for i in commands:
        if i == command_pop:
            n -= 1
            if n < 0:
                return [-1]
            if direction:
                numbers.popleft()
                continue
            numbers.pop()
        elif i == command_reverse:
            if direction:
                direction = 0
            else:
                direction = 1
    if direction:
        return list(numbers)
    return reversed(list(numbers))


T = int(input())
for _ in range(T):
    commands = input()
    n = int(input())
    try:
        numbers = deque(list(map(int, input()[1:-1].split(','))))
    except:
        numbers = []
    answer = run(numbers, n)
    if answer == [-1]:
        print('error')
        continue
    print('[' + ",".join(map(str, answer)) + ']')
    
