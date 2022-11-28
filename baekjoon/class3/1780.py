import sys

input = sys.stdin.readline
answer = [0, 0, 0]


def solution(numbers):
    for i in [-1, 0, 1]:
        if all_is_one(numbers, i):
            answer[i] += 1
            return
    standard = len(numbers) // 3
    cutting_index = [0, standard, standard * 2]
    for i in cutting_index:
        for j in cutting_index:
            solution(cut_arrays(numbers, i, j))


def all_is_one(numbers, number):
    for i in numbers:
        for j in i:
            if j != number:
                return False
    return True


def cut_arrays(numbers, start_row, start_column):
    new_numbers = []
    standard = len(numbers) // 3
    for i in numbers[start_row:start_row + standard]:
        new_numbers.append(i[start_column:start_column + standard])
    return new_numbers


N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))
solution(array)
for i in [-1, 0, 1]:
    print(answer[i])
