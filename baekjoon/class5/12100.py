from collections import deque


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def run(numbers):
    original = len(numbers)
    numbers = list(filter(lambda x: x, numbers))
    N = len(numbers)
    result = []
    k = 0
    for i in range(N):
        if i + k >= N:
            break
        if i + k + 1 == N:
            result.append(numbers[i + k])
            break
        if numbers[i + k] == numbers[i + k + 1]:
            result.append(numbers[i + k] * 2)
            k += 1
            continue
        result.append(numbers[i + k])
    return result + [0] * (original - len(result))


def rotated_0(array):
    result = []
    for i in array:
        result.append(list(i))
    return result


def rotated_90(array):
    n = len(array)
    m = len(array[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = array[i][j]
    return result


def rotated_180(array):
    n = len(array)
    m = len(array[0]) 
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m-j-1][n-i-1] = array[i][j]
    return result


def rotated_270(array):
    n = len(array)
    m = len(array[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - j - 1][i] = array[i][j]
    return result


def new_rotated_180(array):
    return rotated_90(rotated_90(array))


rotate = [(rotated_0, rotated_0), (rotated_90, rotated_270), (new_rotated_180, new_rotated_180), (rotated_270, rotated_90)]


answer = []


def play_copy(array, times):
    if times >= 5:
        maximum = 0
        for i in array:
            for j in i:
                maximum = max(maximum, j)
        answer.append(maximum)
        return
    
    for i, j in rotate:
        result = []
        for k in i(array):
            result.append(run(k))
        for l in j(result):
            print(' '.join(map(str, l)))
        print()
        play_copy(j(result), times + 1)


def play(array, times):
    if times >= 5:
        maximum = 0
        for i in array:
            for j in i:
                maximum = max(maximum, j)
        answer.append(maximum)
        return
    
    for i, j in rotate:
        result = []
        for k in i(array):
            result.append(run(k))
        play(j(result), times + 1)

        
play(board, 0)

print(max(answer))


